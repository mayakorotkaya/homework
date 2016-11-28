word = input('Vvedite slovo: ')
for i in range(len(word)):
    print(word[-i-1::])
