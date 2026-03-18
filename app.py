import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="Rubirizi Tax App", page_icon="🇺🇬")

# 2. This part is your HTML/CSS inside Python
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stHeader { 
        background-color: #1a2a6c; 
        padding: 20px; 
        border-radius: 10px; 
        color: white; 
        text-align: center;
        margin-bottom: 25px;
        border-bottom: 5px solid #f1c40f;
    }
    .reportview-container .main .block-container { padding-top: 2rem; }
    </style>
    <div class="stHeader">
        <h1>Rubirizi Customs Tax Calculator</h1>
        <p>Official URA Import Estimation Tool</p>
    </div>
    """, unsafe_allow_html=True)

# 3. User Inputs (The "Form")
cif_usd = st.number_input("CIF Value (USD)", min_value=0.0, step=100.0)
exchange_rate = st.number_input("Exchange Rate (UGX)", min_value=1.0, value=3800.0)

duty_rate = st.selectbox("Import Duty Rate", 
                         options=[0, 10, 25, 35], 
                         format_func=lambda x: f"{x}%")

apply_wht = st.checkbox("Apply Withholding Tax (6%)", value=True)

# 4. Math Logic
cif_ugx = cif_usd * exchange_rate
import_duty = cif_ugx * (duty_rate / 100)
# VAT is 18% of (CIF + Import Duty)
vat = (cif_ugx + import_duty) * 0.18
wht = cif_ugx * 0.06 if apply_wht else 0
total_taxes = import_duty + vat + wht

# 5. Displaying Results
st.divider()
st.subheader("Tax Breakdown (UGX)")

col1, col2 = st.columns(2)
with col1:
    st.metric("Import Duty", f"{import_duty:,.0f}")
    st.metric("VAT (18%)", f"{vat:,.0f}")

with col2:
    st.metric("WHT (6%)", f"{wht:,.0f}")
    st.info(f"**Total Payable: {total_taxes:,.0f} UGX**")

st.caption("Calculation based on URA standard: VAT = 18% × (CIF + ID)")
