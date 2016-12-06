with open ('quotes.txt', 'r', encoding = 'utf-8') as f:
    text = f.readlines()
end = []
for line in text:
    a = line.split('—')
    if len(a[0].split())<10:
        end.append(a[0])
for el in end:
    print (el)
