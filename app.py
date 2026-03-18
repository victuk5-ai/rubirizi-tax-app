import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Rubirizi Tax Pro", page_icon="🇺🇬", layout="centered")

# 2. Professional Branding & CSS
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stHeader { 
        background-color: #1a2a6c; 
        padding: 25px; 
        border-radius: 12px; 
        color: white; 
        text-align: center;
        border-bottom: 6px solid #f1c40f;
        margin-bottom: 20px;
    }
    .whatsapp-btn {
        background-color: #25D366;
        color: white;
        padding: 15px;
        text-decoration: none;
        border-radius: 10px;
        font-weight: bold;
        display: block;
        text-align: center;
        margin-top: 20px;
    }
    .total-card {
        background-color: #ffffff;
        padding: 20px;
        border-left: 8px solid #d32f2f;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    <div class="stHeader">
        <h1>Rubirizi Customs Tax Calculator</h1>
        <p>Professional URA Import & Motor Vehicle Estimation</p>
        <p style="font-size: 0.9rem; font-weight: bold; color: #f1c40f;">Developed by Victor</p>
    </div>
    """, unsafe_allow_html=True)

# 3. Input Sidebar
st.sidebar.header("Global Settings")
calc_mode = st.sidebar.radio("Clearance Category", ["General Goods", "Motor Vehicle"])
exchange_rate = st.sidebar.number_input("Exchange Rate (1 USD to UGX)", value=3800.0)

# 4. Main Input Form
with st.container():
    cif_usd = st.number_input("Enter CIF Value (USD)", min_value=0.0, step=50.0)
    cif_ugx = cif_usd * exchange_rate

    col_a, col_b = st.columns(2)
    
    with col_a:
        duty_rate = st.selectbox("Import Duty", [0, 10, 25, 35], index=2, format_func=lambda x: f"{x}%")
        infra_levy = st.checkbox("Infrastructure Levy (1.5%)", value=True)
    
    with col_b:
        apply_wht = st.checkbox("Withholding Tax (6%)", value=True)
        if calc_mode == "Motor Vehicle":
            reg_fee = st.number_input("Registration Fee (UGX)", value=1200000)
        else:
            stamp_duty = st.number_input("Stamp Duty/Other (UGX)", value=35000)

# 5. Advanced Logic (Motor Vehicle Age)
env_levy = 0.0
if calc_mode == "Motor Vehicle":
    st.subheader("Vehicle Age Assessment")
    veh_age = st.radio("Age of Vehicle", 
                       ["New to 8 Years", "9 to 14 Years", "15+ Years"], 
                       horizontal=True)
    if "9 to 14" in veh_age:
        env_levy = cif_ugx * 0.35
    elif "15+" in veh_age:
        env_levy = cif_ugx * 0.50

# 6. Final Math Logic
import_duty = cif_ugx * (duty_rate / 100)
infrastructure = (cif_ugx * 0.015) if infra_levy else 0
wht = (cif_ugx * 0.06) if apply_wht else 0

# VAT is 18% of (CIF + Import Duty + Infrastructure Levy)
vat_base = cif_ugx + import_duty + infrastructure
vat = vat_base * 0.18

# Total Calculation
total_fees = import_duty + vat + wht + infrastructure + env_levy
if calc_mode == "Motor Vehicle":
    total_fees += reg_fee
else:
    total_fees += stamp_duty

# 7. Display Results
st.divider()
st.subheader("Detailed Breakdown")

res_col1, res_col2 = st.columns(2)
with res_col1:
    st.write(f"**Import Duty:** {import_duty:,.0f} UGX")
    st.write(f"**VAT (18%):** {vat:,.0f} UGX")
    st.write(f"**Infrastructure (1.5%):** {infrastructure:,.0f} UGX")

with res_col2:
    st.write(f"**WHT (6%):** {wht:,.0f} UGX")
    if calc_mode == "Motor Vehicle":
        st.write(f"**Env. Levy:** {env_levy:,.0f} UGX")
        st.write(f"**Reg. Fees:** {reg_fee:,.0f} UGX")

st.markdown(f"""
    <div class="total-card">
        <h2 style="margin:0; color:#d32f2f;">Total Payable</h2>
        <h1 style="margin:0;">UGX {total_fees:,.0f}</h1>
    </div>
    """, unsafe_allow_html=True)

# 8. WhatsApp Lead Generation
whatsapp_msg = f"Hello Victor, I need a clearance quote for a {calc_mode} with CIF {cif_usd} USD. Total estimate was {total_fees:,.0f} UGX."
whatsapp_url = f"https://wa.me/256741899165?text={whatsapp_msg.replace(' ', '%20')}"

st.markdown(f'<a href="{whatsapp_url}" class="whatsapp-btn">🚀 Hire Victor for Clearance</a>', unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Rubirizi Clearing & Forwarding Agency. This tool provides estimates only.")
