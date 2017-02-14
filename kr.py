with open('text.xml','r', encoding = 'utf-8') as m:
    lines = 4
    for line in m:
        if '</teiHeader>' in line:
            break
        elif '</teiHeader>' not in line:
            lines += 1

with open('file.txt', 'w', encoding = 'utf-8') as f:
    f = lines
print(f)

