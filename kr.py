import os
import re
def chitau():
    folder = 'news'
    words = {}
    for f in os.listdir(folder):
        with open(os.path.join(folder, f), encoding='cp1251') as text:
            text = text.read()
            words[f] = len(re.findall('<w>.+</w>', text))
##            print(f, words)

    with open('new_file', 'w', encoding = 'utf-8') as m:
        for f in words:
            m.write(f+'\t'+str(words[f])+'\n')
chitau()
