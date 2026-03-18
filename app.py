import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="Rubirizi Tax App", page_icon="🇺🇬")

# 2. Professional Header with Victor's Branding
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
    .footer {
        text-align: center;
        padding: 10px;
        font-size: 0.8rem;
        color: #666;
    }
    .whatsapp-btn {
        background-color: #25D366;
        color: white;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
    }
    </style>
    <div class="stHeader">
        <h1>Rubirizi Customs Tax Calculator</h1>
        <p>Official URA Import Estimation Tool</p>
        <p style="font-size: 0.8rem; opacity: 0.8;">Developed by Victor</p>
    </div>
    """, unsafe_allow_html=True)

# 3. User Inputs
cif_usd = st.number_input("CIF Value (USD)", min_value=0.0, step=100.0)
# Updated default rate to 3800
exchange_rate = st.number_input("Exchange Rate (UGX)", min_value=1.0, value=3800.0)

duty_rate = st.selectbox("Import Duty Rate", 
                         options=[0, 10, 25, 35], 
                         index=2,
                         format_func=lambda x: f"{x}%")

apply_wht = st.checkbox("Include WHT (6%)", value=True)

# 4. Math Logic
cif_ugx = cif_usd * exchange_rate
import_duty = cif_ugx * (duty_rate / 100)
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

# 6. Contact Section
st.divider()
st.write("### Need Professional Clearing?")
st.write("Contact **Rubirizi Clearing and Forwarding Agency** for a formal quote.")

# WhatsApp Link for Victor
whatsapp_url = "https://wa.me/256741899165?text=Hello%20Victor,%20I%20used%20your%20Tax%20Calculator%20and%20need%20help%20with%20clearing%20my%20goods."
st.markdown(f'<a href="{whatsapp_url}" class="whatsapp-btn">Chat with Victor on WhatsApp</a>', unsafe_allow_html=True)

st.markdown('<div class="footer">© 2026 Rubirizi Tax App | Authorized Clearing & Forwarding</div>', unsafe_allow_html=True)
