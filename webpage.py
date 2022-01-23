import streamlit as st
import pandas as pd
import numpy as np

st.title('Privacy Helper')

st.sidebar.header("Select a company to view their data policy.")
def user_input_company():
    selection = st.sidebar.selectbox('Company',('Amazon','Facebook', 'Google', 'Grubhub', 'Instagram', 'LinkedIn', 'Snapchat', 'Tiktok', 'Twitch', 'Uber', 'Yahoo'))
    return selection

company = user_input_company()

st.subheader("Here is a sample of the Privacy Policy we are looking at.")

company_file_name = company + 'DataPolicy.txt'
company_file_path = 'privacy_policy_files/' + company_file_name

text = ""

with open(company_file_path, encoding="utf-8") as f:
    for i in range(15):
        text += next(f).strip()

st.markdown(text)

st.subheader("Here is the highlights of the Privacy Policy.")
st.markdown("sample highlights")