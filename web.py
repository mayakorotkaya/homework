#

from flask import Flask
from flask import render_template

app = Flask(__name__)

def reading(text):
    with open(text, 'r', encoding = 'utf-8') as f:
        for line in f:
            lang=f.read()
        #lang=f.read()
            lang=lang.split('	')
            lang=lang.remove(lang[2:])
            v={}
            v[lang[0]]=lang[1]
    return v
    

@app.route('/')
def codeISO():
    return render_template('pagge.html', emails=reading(code.tsv))

if __name__ == '__main__':
    app.run(debug=True)
    
