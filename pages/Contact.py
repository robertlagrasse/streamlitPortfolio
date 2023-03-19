import streamlit as st
st.set_page_config(layout="wide")
st.header('Contact Me')

with st.form(key='form'):
    email = st.text_input("Your Email Address")
    message = st.text_area("Your Message...")
    submit = st.form_submit_button("Submit")
    if submit:
        st.warning("Submit button pressed. ")

ubqkhrqcudmavslg