import streamlit as st

# Set up Streamlit page
st.set_page_config(page_title="Currency Converter",layout="wide")  
st.sidebar.header("Interconvert Thai Baht | Chinese Yuan | USD | Indian Rupee")
st.sidebar.write("Made with ❤️ ")
st.sidebar.write('Powered by Python')
st.header("What currency do you have?")
st.subheader("Seamlessly convert Thai Baht | Chinese Yuan | USD | Indian Rupee")



conv_rate={
    "THB": {"INR":2.30,"CNY": 0.20},  # 1 Thai Baht = 2.30 INR, 0.20 CNY
    "INR": {"THB":0.43,"CNY": 0.086},  # 1 INR = 0.43 THB, 0.086 CNY
    "CNY": {"THB":5.00,"INR": 11.63} } # 1 CNY = 5.00 THB, 11.63 INR


# Select currency
cur_type=st.selectbox("Select Currency Type", ["Thai Baht (THB)", "Indian Rupees (INR)", "Chinese Yuan (CNY)"])
amount=st.number_input("Enter Amount", min_value=0.0, format="%.2f")

# Button Click
ssubmit = st.button("Convert")

# Conversion Logic
if ssubmit:
    if cur_type=="Thai Baht (THB)":
        conv_inr=amount*conv_rate["THB"]["INR"]
        conv_cny=amount*conv_rate["THB"]["CNY"]
        st.subheader("Converted Amounts:")
        st.write(f"**Indian Rupees (INR): ₹{conv_inr:.2f}**")
        st.write(f"**Chinese Yuan (CNY): ¥{conv_cny:.2f}**")

    elif cur_type=="Indian Rupees (INR)":
        conv_thb=amount*conv_rate["INR"]["THB"]
        conv_cny=amount*conv_rate["INR"]["CNY"]
        st.subheader("Converted Amounts:")
        st.write(f"**Thai Baht (THB): ฿{conv_thb:.2f}**")
        st.write(f"**Chinese Yuan (CNY): ¥{conv_cny:.2f}**")

    elif cur_type == "Chinese Yuan (CNY)":
        conv_thb = amount*conv_rate["CNY"]["THB"]
        conv_inr = amount*conv_rate["CNY"]["INR"]
        st.subheader("Converted Amounts:")
        st.write(f" **Thai Baht (THB): ฿{conv_thb:.2f}**")
        st.write(f"**Indian Rupees (INR): ₹{conv_inr:.2f}**")

