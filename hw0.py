import codecs
f = codecs.open('file.txt', 'r', 'utf-8')
text = f.read()
new_text=text.split(' ')
all_words = len('new_text')
long_words = ()
for element in new_text:
    if len(element)>10:
        long_words =+ 1
m = long_words*100/all_words
print(m)
