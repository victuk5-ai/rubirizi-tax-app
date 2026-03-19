
import streamlit as st

st.set_page_content(page_title="Rubirizi Tax Pro", layout="centered")

# --- HEADER ---
st.title("Rubirizi Tax Pro")
st.write("Developed by Victor")
st.divider()

# --- INPUTS ---
col1, col2 = st.columns(2)

with col1:
    calc_type = st.radio("Select Category", ["General Goods", "Motor Vehicle"])
    cif_usd = st.number_input("Enter CIF Value (USD)", min_value=0.0, step=100.0)

with col2:
    exchange_rate = st.number_input("Exchange Rate (UGX)", value=3800.0)
    if calc_type == "Motor Vehicle":
        vehicle_age = st.selectbox("Vehicle Age", ["Under 8 Years", "8 - 14 Years", "Over 15 Years"])

# --- CALCULATIONS ---
cif_ugx = cif_usd * exchange_rate
import_duty = cif_ugx * 0.25
infra_levy = cif_ugx * 0.015

env_levy = 0.0
if calc_type == "Motor Vehicle":
    if vehicle_age == "8 - 14 Years":
        env_levy = cif_ugx * 0.35
    elif vehicle_age == "Over 15 Years":
        env_levy = cif_ugx * 0.50

# VAT Calculation
vat = (cif_ugx + import_duty + infra_levy) * 0.18
wht = cif_ugx * 0.06

total_tax = import_duty + env_levy + infra_levy + vat + wht

# --- DISPLAY ---
st.subheader("Tax Results (UGX)")

res1, res2 = st.columns(2)
with res1:
    st.write(f"**Import Duty:** {import_duty:,.0f}")
    st.write(f"**VAT (18%):** {vat:,.0f}")
    st.write(f"**Infra Levy:** {infra_levy:,.0f}")

with res2:
    if calc_type == "Motor Vehicle":
        st.write(f"**Env. Levy:** {env_levy:,.0f}")
    st.write(f"**WHT (6%):** {wht:,.0f}")

st.success(f"### Total Estimate: {total_tax:,.0f} UGX")

st.divider()

# --- CONTACT ---
st.write("### Need Clearing Services?")
whatsapp_url = "https://wa.me/256706631303?text=I%20need%20clearing%20for%20a%20quote"
st.markdown(f'[💬 Chat with Victor on WhatsApp]({whatsapp_url})')

st.caption("Rubirizi Clearing & Forwarding Agency")
