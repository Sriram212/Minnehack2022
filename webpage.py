from keywordfinder import policy_keywords

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


output = policy_keywords().getKeyWords('keywords.txt', 'stopwords.txt', 'policies.txt', 50)
output += policy_keywords().getKeyWords(keywords_doc=None, stopwords_list='stopwords.txt', policies_text='policies.txt', n_words=20)
companies_list = ['Amazon', 'Facebook', 'Google', 'Grubhub', 'Instagram', 'Linkedin', 'Snapchat', 'Tiktok', 'Uber', 'Yahoo', 'Reddit' ]

for company in companies_list:
    policy_keywords().highlight_doc('%s.html' % (company,), output, 'privacy_policy_files/%sDataPolicy.txt' % (company,))
    print(company)
