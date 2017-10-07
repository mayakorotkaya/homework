import urllib.request
import time
import re
import os
import html


time.sleep(2)



def info(page):
     user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
     req = urllib.request.Request(page, headers={'User-Agent': user_agent})
     with urllib.request.urlopen(req) as response:
         try:
             html = response.read().decode('utf-8')
             regeTitle = re.compile('<meta name="description" content="(.*?)" />', flags=re.DOTALL)
             titles = regeTitle.search(html)
             goodtitle= titles.group(1)
             regAll = re.compile('[a-zA-Z0-9_#;&/\№|=\{\}:\."\?\(\)\-@«»]', re.DOTALL)
             regSpace = re.compile('\s+', re.DOTALL)
             goodtitle = regAll.sub('',goodtitle)
             goodtitle = regSpace.sub('_',goodtitle)
             #print(goodtitle)

             regeDate = re.compile("class='rubrics'></span><span class='date_start'>(.*?)</span>", flags=re.DOTALL)
             dates = regeDate.search(html)
             gooddates = dates.group(1)
             gooddates = gooddates[0:4]+"."+gooddates[5:7]+"."+gooddates[8:10]
             #print(gooddates)

             regeRubrics = re.compile("<span class='rubrics'>(.*?)</span>", flags=re.DOTALL)
             rubrics = regeRubrics.search(html)
             goodrubrics = rubrics.group(1)
             #print(goodrubrics)

             regeAuthor = re.compile("<span class='author'>(.*?)</span>", flags=re.DOTALL)
             authors = regeAuthor.search(html)
             goodauthors = authors.group(1)
             #print(goodauthors)

             regeText = re.compile("span class='text'><p>(.*?)</p></span>", flags=re.DOTALL)
             texts = regeText.search(html)
             goodtexts = texts.group(1)
             regTag = re.compile('<.*?>', re.DOTALL)
             regfu = re.compile('&.*?;', re.DOTALL)
             regAll = re.compile('[a-zA-Z0-9_#;&/\№|=\{\}:\."\?\(\)\-@«»]', re.DOTALL)
             goodtexts = regTag.sub("", goodtexts)
             goodtexts = regfu.sub(" ",goodtexts)
             goodtexts = regAll.sub("", goodtexts)
             #verygoodtexts = html.unescape(goodtexts)
             #print(goodtexts)

             path ='ZARYA/plain/{}/{}/'.format(gooddates[0:4], gooddates[5:7])

             if not os.path.exists(path):
                 os.makedirs(path)
             nametext = path+'{}.txt'.format(goodtitle)
             with open(nametext, 'a') as j:
                if len(goodauthors) == 0:
                    j.write('@au NoName' + '\n')
                else:
                    j.write('@au ' + goodauthors + '\n')
                j.write('@ti ' + goodtitle + '\n')
                j.write('@da ' + gooddates + '\n')
                j.write('@url ' + page + '\n')
                j.write(goodtexts)


             row = '%s\t%s\t\t\t%s\t%s\tпублицистика\t\t\t%s\t\tнейтральный\tн-возраст\tн-уровень\tрайонная\t%s\tЗаря\t\t%s\tгазета\tРоссия\tСмоленский район Алтайский край\tru'

             table = row % (path, goodauthors, goodtitle, gooddates, goodrubrics, page, gooddates[0:4])
             with open('ZARYA/metadata.csv', 'a') as q:
                 q.write(table)

             path2 = 'ZARYA/mystem-xml/{}/{}/'.format(gooddates[0:4], gooddates[5:7])
             if not os.path.exists(path2):
                 os.makedirs(path2)
             path3 = 'ZARYA/mystem-plain/{}/{}/'.format(gooddates[0:4], gooddates[5:7])
             if not os.path.exists(path3):
                 os.makedirs(path3)

             # обрабатываем файлы в mystem
             input = 'ZARYA/plain/{}/{}/{}.txt'.format(gooddates[0:4], gooddates[5:7], goodtitle)
             output = 'ZARYA/mystem-plain/{}/{}/{}.txt'.format(gooddates[0:4], gooddates[5:7], goodtitle)
             output2 = 'ZARYA/mystem-xml/{}/{}/{}.xml'.format(gooddates[0:4], gooddates[5:7], goodtitle)
             os.system("/Users/mayakorotkaya/Downloads/mystem -id" + input + " " + output)
             os.system("/Users/mayakorotkaya/Downloads/mystem -id" + input + " " + output2)



         except AttributeError:
             pass



     



commonUrl = 'http://zariagazeta.ru/?module=articles&action=view&id='
for i in range(1874, 2078):
    pageurl = commonUrl + str(i)
    info(pageurl)






#Старая газета

# mass = []
# commonUrl = 'http://avangard-vavozh.ucoz.ru/news/20'
# for i in range(10, 18):
#     if i == 10:
#         for n in range(11, 13):
#             page = commonUrl + '10' + '-' + str(n)
#     else:
#         pageUrl = commonUrl + str(i)
#         for n in range(1, 13):
#             if len(str(n)) < 2:
#                 page = pageUrl + '-' + '0' + str(n)
#             else:
#                 page = pageUrl + '-' + str(n)
#
#             reg = re.findall('<a class="archiveEntryTitleLink" href="(.*?)">', download_page(page), flags=re.DOTALL)
#             for link in reg:
#                 final_page = 'http://avangard-vavozh.ucoz.ru'+link
#                 mass.append(final_page)
# download_page('http://avangard-vavozh.ucoz.ru/news/2010-11')
# print(mass)
# texts = []
# regTag = re.compile('<.*?>', re.DOTALL)
# regSpace = re.compile('\s{2,}', re.DOTALL)
# regComment = re.compile('<!--.*?-->', re.DOTALL)
# for m in mass:
#     download_page(m)
#     clean_m = regSpace.sub("", m)
#     clean_m = regTag.sub("", clean_m)
#     clean_m = regTag.sub("", clean_m)
#     # clean_m = unescape(m)
#     texts.append(clean_m)
# for t in texts:
#     print(t)






#открываем сайт и печатаем заголовки
# user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
# req = urllib.request.Request('http://avangard-vavozh.ucoz.ru/', headers={'User-Agent':user_agent})
# with urllib.request.urlopen(req) as response:
#    html = response.read().decode('utf-8')
#    regeTitle = re.compile('<div class="eTitle".*?</div>', flags= re.DOTALL)
#    titles = regeTitle.findall(html)
# new_titles = []
# regTag = re.compile('<.*?>', re.DOTALL)
# regSpace = re.compile('\s{2,}', re.DOTALL)
# for t in titles:
#     clean_t = regSpace.sub("", t)
#     clean_t = regTag.sub("", clean_t)
#     new_titles.append(clean_t)
# for t in new_titles:
#     print(t)







