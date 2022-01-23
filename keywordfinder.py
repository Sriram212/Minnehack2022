import yake
from keybert import KeyBERT
import re

#kw_extractor = yake.KeywordExtractor()

text = ""
stopwords = ""
keywords = ""

with open('policies.txt', encoding="utf-8") as f:
    text += f.read()
with open('stopwords.txt', encoding="utf-8") as f:
    stopwords += f.read()
with open('keywords.txt', encoding="utf-8") as f:
    keywords += f.read()
stopwords_list = stopwords.split('\n')
keywords_list = keywords.split('\n')
text = text.lower()

# language = "en"
# max_ngram_size = 1
# deduplication_threshold = 0.9
# numOfKeywords = 50
# custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None, stopwords=stopwords)
# keywords = custom_kw_extractor.extract_keywords(text)
# for kw in keywords:
#     print(kw)

kw_model = KeyBERT()

output = kw_model.extract_keywords(text, candidates=keywords_list, keyphrase_ngram_range=(1, 1), top_n=25, diversity=0.5, stop_words=stopwords_list)

linkedin_text = ""

with open('privacy_policy_files/LinkedinDataPolicy.txt', encoding="utf-8") as f:
    linkedin_text += f.read()

sentences_dict = {}

line_end_chars = "!", "?", '\n'
regexPattern = '|'.join(map(re.escape, line_end_chars))
line_list = re.split(regexPattern, linkedin_text)
for i in output:
    word = i[0]
    count = 0
    for line in line_list:
        if word in line.lower() and count < 3:
            if line not in sentences_dict:
                print(line + '\n')
                sentences_dict[line] = 1
                count += 1

