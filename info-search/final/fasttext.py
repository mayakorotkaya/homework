from gensim.models.keyedvectors import KeyedVectors
from tfidf import preprocessing
import numpy as np

fast_model = 'model.model'
model = KeyedVectors.load(fast_model)

wv = model.wv

def lookup(doc, wv):
    d = preprocessing(doc).split()
    checked = []

    for word in d:
        try:
            word in wv
        except AttributeError:
            continue
        checked.append(wv[word])

    vec = np.mean(checked, axis=0)
    return vec

def cos_sim(v1, v2):
    return np.inner(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


#corpora = 'quora_question_pairs_rus.csv'

import csv


# def get_data(corpora, wv, stop=5000):
#     indexed = []
#     id_to_text = {}
#     query_to_dupl_id = {}
#     counter = 0
#
#     with open(corpora, 'r', encoding='utf-8') as f:
#         r = csv.reader(f)
#         for line in r:
#
#             if line[0] == '':
#                 continue
#
#             _id, text, query, isduplicate = line
#             id_to_text[_id] = text
#
#             if isduplicate == '1':
#                 query_to_dupl_id[query] = _id
#
#             indexed.append(lookup(text, wv))
#
#             counter += 1
#             if counter >= stop:
#                 break
#     return indexed, id_to_text, query_to_dupl_id

#indexed, id_to_text, query_to_dupl_id = get_data(corpora, wv, stop=50000)

import pickle
#with open("Indexed_FT.pickle", 'wb') as f:
#    pickle.dump((indexed, id_to_text, query_to_dupl_id), f)

with open("Indexed_FT.pickle", 'rb') as f:
    indexed, id_to_text, query_to_dupl_id = pickle.load(f)

def search(query, wv, indexed):

    query_v = lookup(query, wv)

    result = {}
    for i, doc_vector in enumerate(indexed):
        score = cos_sim(query_v, doc_vector)
        if type(score) is np.float32:
            result[i] = score

    return sorted(result.items(), key=lambda x: x[1], reverse=True)


def search_fasttext(text):
    ind = search(text, wv, indexed)[:10]
    ar = {}
    for el in ind:
        ar[id_to_text['{}'.format(el[0])]] = el[1]
    return ar
