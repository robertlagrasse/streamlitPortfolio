import streamlit as st
import sendMail
import pandas

df=pandas.read_csv('data/topics.csv')
signature = '''
Brought to you by Grandmaster Groove
Read these lines and shut yo mouth.
    '''

st.set_page_config(layout="wide")
st.header('Contact Me')

with st.form(key='form', clear_on_submit=True):
    email = st.text_input("Your Email Address")
    subject = f"Subject:{st.selectbox('Subject', df['topic'])}\n"
    raw_message = st.text_area("Your Message...")
    submit = st.form_submit_button("Submit")

    header = f"A new webform submission from {email} has arrived\n"
    message = subject + \
              header + \
              raw_message + \
              signature

    if submit:
        sendMail.send(email, message)
        st.info("Your email was sent!")
