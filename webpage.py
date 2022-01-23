from keywordfinder import policy_keywords

output = policy_keywords().getKeyWords('keywords.txt', 'stopwords.txt', 'policies.txt', 50)
output += policy_keywords().getKeyWords(keywords_doc=None, stopwords_list='stopwords.txt', policies_text='policies.txt', n_words=20)
policy_keywords().highlight_doc('web_app/out_policies/in.html', output, 'web_app/out_policies/out.txt')
