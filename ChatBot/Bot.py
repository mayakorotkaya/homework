from pymorphy2 import MorphAnalyzer
import re
import random
from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('question.html')

@app.route('/thanks')
def thanks():
    morph = MorphAnalyzer()
    if request.args:
        #a = input('Введите предложение: ')
        a = request.args['sentence']
        words = open('words.txt','r',encoding='utf-8')
        words = words.readlines()
        reg = re.compile('[^а-яА-Я ]')
        a = a.split()
        new_sent=open('sentence.txt','w',encoding='utf-8')
        for i in a:
            ana = morph.parse(i)[0]
            random.shuffle(words)
            for word in words:
                word = reg.sub('', word)
                word = morph.parse(word)[0]
                if word.tag == ana.tag:
                    new_sent.write(word.word)
                    new_sent.write(' ')
                    break
        new_sent.close()
        new_sent1 = open('sentence.txt','r',encoding='utf-8')
        new_sent1=new_sent1.read()
        return render_template('thanks.html', sentence_answer=new_sent1)
        #print(new_sent1)
        #new_sent1.close()
    return redirect(url_for(''))

if __name__ == '__main__':
    app.run(debug=True)
