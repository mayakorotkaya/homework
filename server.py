import urllib.request
import ssl
import json
import key
import re
from collections import Counter

ssl._create_default_https_context = ssl._create_unverified_context
stroka = 'https://api.vk.com/method/wall.get?owner_id=99657081&count=10&v=5.73&access_token={}'.format(key.secret_key)
req = urllib.request.Request(stroka)
response = urllib.request.urlopen(req)
result = response.read().decode('utf-8')
#print(result)
data = json.loads(result)
f = open('text.txt', 'w')
i = -1
for m in range(9):
    i += 1
    f.write(data["response"]["items"][i]["text"])
f.close()
g = open('text.txt', 'r')
g = g.read()
regAll = re.compile('[a-zA-Z0-9_#;&/\№|=\{\}:\."\?\(\)\-@!,«»🌸🌸🌸☀️☀️☀️✨🌟⭐️❤️❤️💛💚💙💕💓]', re.DOTALL)
g = regAll.sub(" ", g)
g = g.split()
#cntr = Counter(g)
#print(cntr)
chastot={}
z = 0
for elem in g:
    if elem in chastot:
        chastot[elem]+=1
    else:
        chastot[elem]=1
print(chastot)