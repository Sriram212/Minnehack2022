import yake
from keyBERT import KeyBERT
import re
from keyBERT._highlight import highlight_document
from nltk.corpus import stopwords as list_of_eng_stopwords

class policy_keywords:
    def getKeyWords(self, keywords_doc=None, stopwords_list=None, policies_text=None, n_words=None):
        text = ""
        stopwords = ""
        keywords = ""

        with open(policies_text, encoding="utf-8") as f:
            text += f.read()
        f.close()
        with open(stopwords_list, encoding="utf-8") as f:
            stopwords += f.read()
        f.close()
        keywords_list = None
        if keywords_doc is not None:
            with open(keywords_doc, encoding="utf-8") as f:
                keywords += f.read()
            f.close()
            keywords_list = keywords.split('\n')
        stopwords_list = stopwords.split('\n')
        text = text.lower()

        output = KeyBERT.extract_keywords(KeyBERT(), docs=text, candidates=keywords_list, keyphrase_ngram_range=(1, 1), top_n=n_words, diversity=0.1, stop_words=stopwords_list)
        return output

    def highlight_doc(self, html_doc_to_write, keywords, policy):
        policy_text = ""

        with open(policy, encoding="utf-8") as f:
            policy_text += f.read()
        f.close()

        highlighted_document = highlight_document(policy_text, keywords)

        line_end_chars = "! ", "?", '. ', '<br>', ';<br>'
        regexPattern = '|'.join(map(re.escape, line_end_chars))
        line_list = re.split(regexPattern, highlighted_document)

        f = open(html_doc_to_write, 'w')
        f.write('<p>')

        for line in line_list:
            if '<span style' in line:
                f.write(line + '.<br><br>')

        f.write('</p>')
        f.close()

