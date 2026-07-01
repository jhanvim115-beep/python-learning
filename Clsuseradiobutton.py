# import the streamlit library 
import streamlit as st 
# give a title to our app 
st.title('Mini Calculator') 
# TAKE INPUT 
n1 = st.number_input("Enter n1") 
n2 = st.number_input("Enter n2") 
action = st.radio('Select your action: ', ('Sum', 'Sub', 'Mul', 'Div'), horizontal=True) 
if (action == 'Sum'): 
    ans = n1 + n2 
    st.success("Sum is {}.".format(ans)) 
if (action == 'Sub'): 
    ans = n1 - n2 
    st.success("Subtraction is {}.".format(ans)) 
if (action == 'Mul'): 
    ans = n1 * n2 
    st.success("Multiplication is {}.".format(ans)) 
if (action == 'Div'): 
    ans = n1 / n2 
    st.success("Division is {}.".format(ans))