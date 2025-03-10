import streamlit as st

# Setting up Streamlit page
st.set_page_config(page_title="Currency Converter",layout="wide")  
st.sidebar.header("Interconvert Thai Baht | Chinese Yuan | USD | Indian Rupee")
st.sidebar.write("Made with ❤️ ")
st.sidebar.write('Powered by Python')
st.header("What currency do you have?")
st.subheader("Seamlessly interconvert Thai Baht | Chinese Yuan | USD | Indian Rupee")



conv_rate={

"THB": {"INR": 2.3, "CNY": 0.2, "USD": 0.028},
    "INR": {"THB": 0.43, "CNY": 0.088, "USD": 0.012},
    "CNY": {"THB": 4.9, "INR": 11.36, "USD": 0.14},
    "USD": {"THB": 35.5, "INR": 83.0, "CNY": 7.1}}


# Select currency
cur_type=st.selectbox("Select Currency Type", ["Thai Baht (THB)", "Indian Rupees (INR)",
  "US Dollars(USD)","Chinese Yuan(CNY)"])
amount=st.number_input("Enter Amount", min_value=0.0, format="%.2f")

# Button Click
ssubmit = st.button("Convert")

# Conversion Logic
if ssubmit:
    if cur_type=="Thai Baht (THB)":
        conv_inr=amount*conv_rate["THB"]["INR"]
        conv_cny=amount*conv_rate["THB"]["CNY"]
        conv_usd=amount*conv_rate["THB"]["USD"]
        st.subheader("Converted Amounts:")
        st.write(f"**Indian Rupees (INR): ₹{conv_inr:.2f}**")
        st.write(f"**Chinese Yuan (CNY): ¥{conv_cny:.2f}**")
        st.write(f"**US Dollars (USD):${conv_usd:.2f}**")

    elif cur_type=="Indian Rupees (INR)":
        conv_thb=amount*conv_rate["INR"]["THB"]
        conv_cny = amount*conv_rate["INR"]["CNY"]
        conv_usd=amount*conv_rate["INR"]["USD"]
        st.subheader("Converted Amounts:")
        st.write(f"**Thai Baht (THB): ฿{conv_thb:.2f}**")
        st.write(f"**Chinese Yuan (CNY): ¥{conv_cny:.2f}**")
        st.write(f"**US Dollars (USD):${conv_usd:.2f}**")

    elif cur_type == "Chinese Yuan (CNY)":
        conv_thb = amount*conv_rate["CNY"]["THB"]
        conv_inr = amount*conv_rate["CNY"]["INR"]
        conv_usd=amount*conv_rate["CNY"]["USD"]
        st.subheader("Converted Amounts:")
        st.write(f" **Thai Baht (THB): ฿{conv_thb:.2f}**")
        st.write(f"**Indian Rupees (INR): ₹{conv_inr:.2f}**")
        st.write(f"**US Dollars (USD):${conv_usd:.2f}**")


    elif cur_type =="US Dollars(USD)":
        conv_thb = amount*conv_rate["USD"]["THB"]
        conv_inr = amount*conv_rate["USD"]["INR"]
        conv_cny = amount * conv_rate["USD"]["CNY"]

        st.subheader("Converted Amounts:")
        st.write(f" **Thai Baht (THB): ฿{conv_thb:.2f}**")
        st.write(f"**Indian Rupees (INR): ₹{conv_inr:.2f}**")
        st.write(f"**Chinese Yuan (CNY): ¥{conv_cny:.2f}**")
        
