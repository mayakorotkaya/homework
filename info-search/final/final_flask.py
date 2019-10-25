from flask import Flask
from flask import url_for, render_template, request, redirect
from tfidf import searchTFIDF
from fasttext import search_fasttext
from bm25 import searchBM25

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('question.html')


@app.route('/thanks')
def thanks():
    if request.args:
        a = request.args['sentence']
        new_sent = []
        if request.args['method'] == 'tfidf':
            for i in searchTFIDF(a):
                i = str(i[0]) + ' - ' + str(i[1])
                new_sent.append({'body': i})
        elif request.args['method'] == 'BM25':
            for k in searchBM25(a):
                k = str(k[0]) + ' - ' + str(k[1])
                new_sent.append({'body': k})
        else:
            for z in search_fasttext(a):
                z = str(z) + ' - ' + str(search_fasttext(a)[z])
                new_sent.append({'body': z})
        return render_template('thanks.html', sentence_answer=new_sent)
    return redirect(url_for(''))

if __name__ == '__main__':
    app.run(debug=True)