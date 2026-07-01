import streamlit as st

st.set_page_config(page_title="Smart GST Calculator", page_icon="💸", layout="centered")

st.title("💸 Smart GST Calculator")

st.divider()

mode = st.radio(
    "Select Calculation Type",
    ["GST Exclusive", "GST Inclusive"],
    horizontal=True
)

amount = st.number_input(
    "Enter Amount (₹)",
    min_value=0.0,
    value=1000.0,
    step=100.0
)

gst_rate = st.slider(
    "Select GST Rate (%)",
    0,
    28,
    18
)

st.divider()

if st.button(" Calculate", use_container_width=True):

    if mode == "GST Exclusive":
        gst_amount = amount * gst_rate / 100
        final_amount = amount + gst_amount
        base_amount = amount

    else:
        base_amount = amount / (1 + gst_rate / 100)
        gst_amount = amount - base_amount
        final_amount = amount

    cgst = gst_amount / 2
    sgst = gst_amount / 2

    st.success("Calculation Completed Successfully!")

    col1, col2 = st.columns(2)

    col1.metric(" Base Amount", f"₹ {base_amount:.2f}")
    col2.metric(" GST Amount", f"₹ {gst_amount:.2f}")

    col3, col4 = st.columns(2)

    col3.metric(" CGST", f"₹ {cgst:.2f}")
    col4.metric(" SGST", f"₹ {sgst:.2f}")

    st.metric(" Final Amount", f"₹ {final_amount:.2f}")

    st.progress(min(gst_rate / 28, 1.0))

    st.balloons()

st.divider()
st.caption("✨ Created using Streamlit")