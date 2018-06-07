import urllib.request
import re
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
req = urllib.request.Request('http://avangard-vavozh.ucoz.ru/', headers={'User-Agent':user_agent})
with urllib.request.urlopen(req) as response:
   html = response.read().decode('utf-8')
   regeTitle = re.compile('<div class="eTitle".*?</div>', flags= re.DOTALL)
   titles = regeTitle.findall(html)
new_titles = []
regTag = re.compile('<.*?>', re.DOTALL)
regSpace = re.compile('\s{2,}', re.DOTALL)
for t in titles:
    clean_t = regSpace.sub("", t)
    clean_t = regTag.sub("", clean_t)
    new_titles.append(clean_t)
for t in new_titles:
    print(t)
