import streamlit as st

# 1. THIS MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_content(
    page_title="Rubirizi Tax Pro",
    page_icon="⚖️",
    layout="centered"
)

# 2. NOW WE ADD THE CSS AND OTHER STUFF
st.markdown(
    """
    <style>
    /* Prevents accidental pull-to-refresh on mobile */
    html, body, [data-testid="stAppViewContainer"] {
        overscroll-behavior-y: contain;
        scroll-behavior: smooth;
    }
    
    /* Support for Dark/Light Mode visibility on the Total Box */
    .total-container {
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #25D366;
        background-color: rgba(151, 151, 151, 0.1);
        margin: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- HEADER ---
st.title("⚖️ Rubirizi Tax Pro")
st.caption("Developed by Victor | Rubirizi Clearing & Forwarding Agency")
st.divider()

# --- INPUTS ---
col1, col2 = st.columns(2)
with col1:
    calc_type = st.radio("Calculation Type", ["General Goods", "Motor Vehicle"])
    cif_usd = st.number_input("Enter CIF Value (USD):", min_value=0.0, format="%.2f")

with col2:
    exchange_rate = st.number_input("Exchange Rate (UGX):", value=3800.0)
    if calc_type == "Motor Vehicle":
        vehicle_age = st.selectbox("Vehicle Age", ["Under 8 Years", "8 - 14 Years", "Over 15 Years"])

# --- CALCULATION LOGIC ---
cif_ugx = cif_usd * exchange_rate
import_duty = cif_ugx * 0.25
infra_levy = cif_ugx * 0.015
env_levy = 0.0

if calc_type == "Motor Vehicle":
    if vehicle_age == "8 - 14 Years":
        env_levy = cif_ugx * 0.35
    elif vehicle_age == "Over 15 Years":
        env_levy = cif_ugx * 0.50

vat = (cif_ugx + import_duty + infra_levy) * 0.18
wht = cif_ugx * 0.06
total_tax = import_duty + env_levy + infra_levy + vat + wht

# --- DISPLAY RESULTS ---
st.subheader("Tax Breakdown (UGX)")

res_col1, res_col2 = st.columns(2)
with res_col1:
    st.write(f"**Import Duty (25%):** {import_duty:,.0f}")
    st.write(f"**VAT (18%):** {vat:,.0f}")
with res_col2:
    st.write(f"**Infra Levy (1.5%):** {infra_levy:,.0f}")
    if calc_type == "Motor Vehicle":
        st.write(f"**Env. Levy:** {env_levy:,.0f}")
    st.write(f"**WHT (6%):** {wht:,.0f}")

st.markdown(f"""
<div class="total-container">
    <p style="margin:0; font-size:1.2em;">Total Estimate</p>
    <h1 style="margin:0; color:#25D366;">{total_tax:,.0f} UGX</h1>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- CALL TO ACTION ---
st.subheader("Ready to Clear?")
whatsapp_link = "https://wa.me/256706631303?text=Hello%20Victor,%20I%20have%20a%20tax%20estimate%20and%20need%20clearing%20services."

st.markdown(f'''
    <a href="{whatsapp_link}" target="_blank" style="text-decoration:none;">
        <div style="width:100%; height:55px; border-radius:12px; background-color:#25D366; color:white; display:flex; align-items:center; justify-content:center; font-size:18px; font-weight:bold;">
            💬 Hire Victor for Clearance
        </div>
    </a>
    ''', unsafe_allow_html=True)

# Navigation helper
if st.button("↑ Back to Top"):
    st.components.v1.html("<script>window.parent.scrollTo(0,0);</script>", height=0)
