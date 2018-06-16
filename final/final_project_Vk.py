# Веб-сервис: пользователь даёт id пользователя в ВК,
# программа скачивает его стену
# и строит граф совместной встречаемости полнозначных слов в окне 3,
# пользователю возвращает визуализацию и основную информацию о графе
import urllib.request
import ssl
import json
import re
import pymorphy2
#import nltk
from pymorphy2 import MorphAnalyzer
from flask import Flask
from flask import url_for, render_template, request, redirect
import networkx as nx
import matplotlib.pyplot as plt
morph = MorphAnalyzer()

ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('question.html')

@app.route('/thanks')
def thanks():
    if request.args:
        id = request.args['id']
        f=open('post_comment.txt','w')
        try:
            offsets = [0, 20]
            for off in offsets:
                stroka1 = 'https://api.vk.com/method/wall.get?owner_id='+str(id)+'&count=20&v=5.73&access_token=4e4390334e4390334e439033504e21bc6044e434e4390331552d00d82502b3b1e852732&offset='+ str(off)
                req = urllib.request.Request(stroka1)
                response = urllib.request.urlopen(req)
                result = response.read().decode('utf-8')
                #print(result)
                if off == 0:
                    data = json.loads(result)
                else:
                    data1 = json.loads(result)
                    needed_data = data1['response']['items']
                    for n in needed_data:
                        data['response']['items'].append(n)
            #print(len(data['response']['items']))
            #print(type(data))
            for m in range(39):
                f.write(data["response"]["items"][m]["text"])
                f.write('\n')
                post = data["response"]["items"][m]["id"]
                for off in offsets:
                    stroka = 'https://api.vk.com/method/wall.getComments?owner_id='+str(id)+'&access_token=4e4390334e4390334e439033504e21bc6044e434e4390331552d00d82502b3b1e852732&post_id='+str(post)+'&count=100&v=5.73&offset='+str(off)
                    requ = urllib.request.Request(stroka)
                    response1 = urllib.request.urlopen(requ)
                    result1 = response1.read().decode('utf-8')
                    if off == 0:
                        data2 = json.loads(result1)
                        for r in range(len(data2['response']['items'])):
                            f.write(data2['response']['items'][r]['text'])
                            f.write('\n')
                    else:
                        data3 = json.loads(result1)
                        for z in range(len(data3['response']['items'])):
                            f.write(data3['response']['items'][z]['text'])
                            f.write('\n')
                        #print(data3)
            f.close()
        except KeyError:
            return render_template('wrong.html')
        m = open('post_comment.txt','r')
        m = m.read()
        m = m.replace('!','.')
        m = m.replace('?','.')
        m = m.replace('\n','.')
        m = m.lower()
        m = m.split('.')
        regPunct = re.compile('[^\w]*$', re.DOTALL)
        regOther = re.compile('[a-zA-Z0-9_#;,\>%&/\№|=\{\}:\.\[\]"\?\(\)\@«»]', re.DOTALL)
        regTire = re.compile(' — ', re.DOTALL)
        all_elems = []
        for i in m:
            new_words = []
            clean_i = regPunct.sub("", i)
            clean_i = regOther.sub("", clean_i)
            clean_i = regTire.sub(" ", clean_i)
            new_words.append(clean_i.split())
            all_elems.append(new_words)

        g = open('stopwords.txt', 'r')
        g = g.read()
        g = g.split()



        for elem in all_elems:
            for i in elem:
                for word in i:
                    ana = morph.parse(word)
                    first = ana[0]
                    for stop in g:
                        if first.normal_form == stop:
                            try:
                                #print(first.normal_form)
                                index_w = i.index(word)
                                del i[index_w]
                            except ValueError:
                                pass

        for elem in all_elems:
            for i in elem:
                if len(i) == 0:
                    try:
                        all_elems.remove(elem)
                    except ValueError:
                        pass

        N = nx.Graph()

        for elem in all_elems:
            for i in elem:
                dict = {}
                for word in i:
                    dict[i.index(word)]= word
                    for elem1 in all_elems:
                        for i1 in elem1:
                            dict1 = {}
                            for word1 in i1:
                                dict1[i1.index(word1)] = word1
                                #if len(N.nodes()) <= 50:
                                if word == word1:
                                    N.add_node(word)
                                    N.add_node(dict.get(i.index(word)+1))
                                    N.add_node(dict.get(i.index(word)-1))
                                    N.add_node(dict1.get(i1.index(word1)+1))
                                    N.add_node(dict1.get(i1.index(word1) - 1))
                                    N.add_edge(word, dict1.get(i.index(word)+1))
                                    N.add_edge(word, dict1.get(i.index(word)-1))
                                    N.add_edge(word, dict1.get(i1.index(word1)+1))
                                    N.add_edge(word, dict1.get(i1.index(word1)-1))
        N.remove_node(None)
        pos = nx.spring_layout(N)
        nx.draw_networkx_nodes(N, pos, node_color='red', node_size=10)
        nx.draw_networkx_edges(N, pos, edge_color='blue')
        nx.draw_networkx_labels(N, pos, font_size=8, font_family='Arial')
        plt.axis('off')
        plt.savefig('static/graph.png', dpi=300, format='png')
        nodes = N.number_of_nodes()
        edges = N.number_of_edges()
        return render_template('thanks.html', nodes=nodes, edges = edges)
        #plt.show()
    return redirect(url_for(''))

if __name__ == '__main__':
    app.run(debug=True)




