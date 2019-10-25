from tfidf import preprocessing
import pandas as pd
import numpy
import operator

# all_text = []
# numb = 0
# import csv
# with open('/Users/mayakorotkaya/infosearch/quora_question_pairs_rus.csv') as qd:
#    qd = csv.reader(qd, delimiter=',')
#    for raw in qd:
#        numb += 1
#        if numb < 502 and numb >= 2:
#            all_text.append(raw)
#
# docs = []
# for i in all_text:
#    if preprocessing(i[2]) != '':
#        docs.append(preprocessing(i[2]))
#    else:
#        docs.append('ы')
#
# corpus = docs
#
# from math import log
#
# k = 2.0
# b = 0.75
# N = len(docs)
#
# l = 0
# for i in docs:
#    l += len(i.split())
# avgdl = l/N
#
# def bm25(D, Q):
#     D = D.split()
#     score = 0
#     n = 0
#     for document in docs:
#         if Q in document:
#             n += 1
#     IDF = log((N - n + 0.5)/(n+0.5))
#     TF = 0
#     for word in D:
#         if word == Q:
#             TF += 1
#     TF = TF/len(D)
#     score += IDF*((TF*(k + 1))/(TF + (k*(1 - b + (b*(len(D)/avgdl))))))
#     return score
#
# import re
# words = {}
# for i in docs:
#     i = i.split()
#     for z in i:
#         z = re.sub(' ', '', z)
#         words[z] = 1
#
# unique_words = []
# for w in words.keys():
#     unique_words.append(w)
#
#
# bm25_matrix = numpy.zeros((500, 1465))
#
# for doc_id, text in enumerate(corpus):
#     for word_id, word in enumerate(unique_words):
#         try:
#             score = bm25(text, word)
#             bm25_matrix[doc_id, word_id] = float(score)
#
#         except KeyError:
#             pass
#
#
import pickle
# with open("Indexed_bm.pickle", 'wb') as f:
#     pickle.dump((unique_words, corpus, bm25_matrix, all_text), f)

with open("Indexed_bm.pickle", 'rb') as f:
    unique_words, corpus, bm25_matrix, all_text = pickle.load(f)

def hotenc(query):
    query = preprocessing(query)
    query = query.split()
    vec = []
    for i in unique_words:
        if i in query:
            vec.append(1)
        else:
            vec.append(0)
    df_query = pd.DataFrame(vec, index=unique_words)
    return df_query


def searchBM25(qu):
    qu = hotenc(preprocessing(qu))
    e = bm25_matrix.dot(qu)
    df_bm = pd.DataFrame(e, index=corpus)
    dict_bm = {}
    for i in range(len(corpus)):
        dict_bm[all_text[i][2]] = df_bm[0][i]
    sorted_bm = sorted(dict_bm.items(), key=lambda x: x[1], reverse=True)
    return sorted_bm[:10]