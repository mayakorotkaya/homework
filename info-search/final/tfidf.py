import re
import nltk
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
nltk.download("stopwords")
from nltk.corpus import stopwords
russian_stopwords = stopwords.words("russian")
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
import operator

normal_forms = []
def preprocessing(text):
    text = str(text)
    text = re.sub(r'[0-9\ufeff]', r'', text)
    normal_text = ''
    for t in tokenizer.tokenize(text):
                t = morph.parse(t)[0]
                if t.normal_form not in russian_stopwords and t.normal_form != 'это' and t.normal_form != 'весь' and not re.match(r'[0-9A-Za-z]', t.normal_form):
                    normal_form = t.normal_form + ' '
                    normal_text += normal_form
    return normal_text


# all_text = []
# numb = 0
# import csv
# with open('/Users/mayakorotkaya/infosearch/quora_question_pairs_rus.csv') as qd:
#     qd = csv.reader(qd, delimiter=',')
#     for raw in qd:
#         numb += 1
#         if numb < 10002 and numb >= 2:
#             all_text.append(raw)
#
# docs = []
# for i in all_text:
#     if preprocessing(i[2]) != '':
#         docs.append(preprocessing(i[2]))
#     else:
#         docs.append('ы')

import pandas as pd
#
from sklearn.feature_extraction.text import TfidfVectorizer
#
# corpus = docs
#
vect = TfidfVectorizer()
# X = vect.fit_transform(corpus)

import pickle
#with open("Indexed_tfidf.pickle", 'wb') as f:
#    pickle.dump((corpus, X, all_text), f)

with open("Indexed_tfidf.pickle", 'rb') as f:
    corpus, X, all_text = pickle.load(f)

X = vect.fit_transform(corpus)

def searchTFIDF(qu):
    qu = vect.transform([preprocessing(qu)]).transpose()
    e = X.dot(qu)
    df_tfIdf = pd.DataFrame(e.toarray(), index=corpus)
    dict_tfIdf = {}
    for i in range(len(corpus)):
        dict_tfIdf[all_text[i][2]] = df_tfIdf[0][i]
    sorted_tfidf = sorted(dict_tfIdf.items(), key=lambda x: x[1], reverse=True)
    return sorted_tfidf[:10]