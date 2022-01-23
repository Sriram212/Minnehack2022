import yake
from keybert import KeyBERT
import re
from keybert._highlight import highlight_document

def write_yellow(f, str_):
    f.write('<span style="background-color: #FFFF00">%s</span>' % str_)

# def substring_in_string(list, word):
#     for x in list:
#         if x.startswith(word) and len(word) > 3:
#             return True
#     return False

#kw_extractor = yake.KeywordExtractor()

text = ""
stopwords = ""
keywords = ""

with open('policies.txt', encoding="utf-8") as f:
    text += f.read()
f.close()
with open('stopwords.txt', encoding="utf-8") as f:
    stopwords += f.read()
f.close()
with open('keywords.txt', encoding="utf-8") as f:
    keywords += f.read()
f.close()
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

output = kw_model.extract_keywords(text, candidates=keywords_list, keyphrase_ngram_range=(1, 1), top_n=71, diversity=0.1, stop_words=stopwords_list)

list_keywords = []
for temp in output:
    list_keywords.append(temp[0])
list_keywords.sort()
print(list_keywords)

linkedin_text = ""

with open('privacy_policy_files/AmazonDataPolicy.txt', encoding="utf-8") as f:
    linkedin_text += f.read()
f.close()

sentences_dict = {}

highlighted_document = highlight_document(linkedin_text, output)

line_end_chars = "! ", "?", '. ', '\n', ';', ' \n'
regexPattern = '|'.join(map(re.escape, line_end_chars))
line_list = re.split(regexPattern, highlighted_document)

f = open('out.html', 'w')
f.write('<html>')
f.write('<p>')

for line in line_list:
    if '<span style' in line:
        f.write(line)

# for i in output:
#     word = i[0]
#     count = 0
#     for line in line_list:
#         if word in line.lower() and count < 3:
#             if line not in sentences_dict:
#                 for x in line.split():
#                     if x in list_keywords:
#                         write_yellow(f, x)
#                         f.write(' ')
#                     else:
#                         f.write(x + ' ')
#                 sentences_dict[line] = 1
#                 count += 1
#                 f.write('.<br><br>')
f.write('</p>')
f.write('</html>')
f.close()

