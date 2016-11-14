word = input ('Vvedite latinskoe slovo: ') 
words = [] 
while word: 
    words.append(word) 
    word = input ('Vvedite latinskoe slovo: ') 
for n in words : 
    if word[-1]=='r' and word[-2]=='u' and word[-3]=='r': 
     print (n)
