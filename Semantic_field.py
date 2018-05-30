import gensim
import urllib.request
import matplotlib.pyplot as plt
import networkx as nx

urllib.request.urlretrieve('http://rusvectores.org/static/models/rusvectores4/RNC/ruscorpora_upos_skipgram_300_5_2018.vec.gz','ruscorpora_1_300_10.vec.gz')
m = 'ruscorpora_1_300_10.vec.gz'
if m.endswith('.vec.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=False)
elif m.endswith('.bin.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True)
else:
    model = gensim.models.KeyedVectors.load(m)
model.init_sims(replace=True)

words = ['шкатулка_NOUN', 'ларец_NOUN', 'комод_NOUN', 'сундук_NOUN']

G = nx.Graph()

for word in words:
    G.add_node(word)
    for i in model.most_similar(positive=[word], topn=10):
        if i[1]>=0.5:
            G.add_node(i[0])
            G.add_edge(i[0],word)

pos=nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='red', node_size=50)
nx.draw_networkx_edges(G, pos, edge_color='blue')
nx.draw_networkx_labels(G, pos, font_size=8, font_family='Arial')
plt.axis('off')
plt.show()

deg = nx.degree_centrality(G)
for nodeid in sorted(deg, key=deg.get, reverse=True):
    print('Самое центральное слово: ',nodeid)
    break

print('Радиус графа: ',nx.radius(G))
print('Коэффициент кластеризации: ',nx.average_clustering(G))

