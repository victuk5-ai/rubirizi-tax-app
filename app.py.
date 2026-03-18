import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Rubirizi Customs Tax Calculator", page_icon="🇺🇬")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stButton>button { width: 100%; background-color: #1a2a6c; color: white; border-radius: 5px; }
    .result-box { padding: 20px; background-color: white; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_input=True)

st.title("🇺🇬 Rubirizi Customs Tax Calculator")
st.write("Estimate your URA Import Taxes accurately.")

# --- Sidebar Inputs ---
with st.sidebar:
    st.header("Input Details")
    cif_usd = st.number_input("CIF Value (USD)", min_value=0.0, step=100.0)
    exchange_rate = st.number_input("Exchange Rate (UGX)", min_value=1.0, value=3800.0)
    
    duty_rate = st.selectbox("Import Duty Rate", 
                             options=[0, 10, 25, 35], 
                             format_func=lambda x: f"{x}%")
    
    apply_wht = st.checkbox("Apply Withholding Tax (6%)", value=True)

# --- Calculation Logic ---
# 1. Convert CIF to UGX
cif_ugx = cif_usd * exchange_rate

# 2. Calculate Import Duty (ID)
import_duty = cif_ugx * (duty_rate / 100)

# 3. Calculate VAT (Standard 18% on CIF + ID)
vat_base = cif_ugx + import_duty
vat = vat_base * 0.18

# 4. Calculate WHT (6% on CIF)
wht = cif_ugx * 0.06 if apply_wht else 0

# 5. Total Taxes
total_taxes = import_duty + vat + wht

# --- Display Results ---
st.subheader("Tax Breakdown (UGX)")

col1, col2 = st.columns(2)

with col1:
    st.metric("Import Duty", f"{import_duty:,.0f}")
    st.metric("VAT (18%)", f"{vat:,.0f}")

with col2:
    st.metric("WHT (6%)", f"{wht:,.0f}")
    st.metric("Total Payable", f"{total_taxes:,.0f}", delta_color="inverse")

st.info(f"**Total Taxable Value (CIF in UGX):** {cif_ugx:,.0f}")

# --- Footer Disclaimer ---
st.divider()
st.caption("Disclaimer: This tool is for estimation purposes for clearing agents and importers. Refer to Asycuda World for official URA assessments.")
