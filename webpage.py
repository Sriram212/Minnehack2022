import streamlit as st
import pandas as pd
import numpy as np
from keybert import KeyBERT

# st.title('Privacy Helper')

# st.sidebar.header("Select a company to view their data policy.")
# def user_input_company():
#     selection = st.sidebar.selectbox('Company',('Amazon','Facebook', 'Google', 'Grubhub', 'Instagram', 'LinkedIn', 'Snapchat', 'Tiktok', 'Twitch', 'Uber', 'Yahoo'))
#     return selection

# company = user_input_company()

# st.subheader("Here is a sample of the Privacy Policy we are looking at.")

# company_file_name = company + 'DataPolicy.txt'
# company_file_path = 'privacy_policy_files/' + company_file_name

# text = ""

# with open(company_file_path, encoding="utf-8") as f:
#     for i in range(15):
#         text += next(f).strip()

# st.markdown(text)

# st.subheader("Here is the highlights of the Privacy Policy.")
# st.markdown("sample highlights")


doc = """
         Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs. It infers a
         function from labeled training data consisting of a set of training examples.
         In supervised learning, each example is a pair consisting of an input object
         (typically a vector) and a desired output value (also called the supervisory signal). 
         A supervised learning algorithm analyzes the training data and produces an inferred function, 
         which can be used for mapping new examples. An optimal scenario will allow for the 
         algorithm to correctly determine the class labels for unseen instances. This requires 
         the learning algorithm to generalize from the training data to unseen situations in a 
         'reasonable' way (see inductive bias).
      """
kw_model = KeyBERT()

f = open('out.html', 'w')
f.write('<html><p>')
f.write(kw_model.extract_keywords(doc, highlight=True))

f.write('</p></html>')
f.close

# keywords = kw_model.extract_keywords(doc, highlight=True)
# st.text(keywords)
# st.markdown(keywords)