import streamlit as st

st.title("🍕 Restaurant Bill Calculator")

food_bill = st.number_input("Enter Food Bill (₹)", min_value=0.0)

gst = st.selectbox("Select GST (%)", [5, 12, 18])

service_charge = st.number_input("Service Charge (%)", min_value=0.0)

tip = st.number_input("Tip Amount (₹)", min_value=0.0)

if st.button("Calculate Bill"):

    gst_amount = (food_bill * gst) / 100
    service_amount = (food_bill * service_charge) / 100

    final_bill = food_bill + gst_amount + service_amount + tip

    st.subheader("Bill Details")

    st.write("Food Bill : ₹", food_bill)
    st.write("GST Amount : ₹", round(gst_amount, 2))
    st.write("Service Charge : ₹", round(service_amount, 2))
    st.write("Tip : ₹", tip)

    st.success(f"Final Bill = ₹ {round(final_bill,2)}")