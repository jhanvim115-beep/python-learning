import streamlit as st 
# give a title to our app 
st.title('Mini Calculator') 
# TAKE  INPUT 
n1 = st.number_input("Enter n1") 
n2 = st.number_input("Enter n2") 
col1, col2, col3, col4 = st.columns(4) 
with col1: 
    Sum = st.button('Sum') 
with col2: 
    Sub = st.button('Sub') 
with col3: 
    Mul = st.button('Mul') 
with col4: 
    Div = st.button('Div') 
    if Sum: 
        ans = n1 + n2 
        st.text("Sum is  {}.".format(ans)) 
    if Sub: 
        ans = n1 - n2 
        st.text("Subtraction is  {}.".format(ans)) 
    if Mul: 
        ans = n1 * n2 
        st.text("Multiplication is  {}.".format(ans)) 
    if Div: 
        ans = n1 / n2 
        st.text("Division is  {}.".format(ans))