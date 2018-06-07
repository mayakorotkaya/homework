import urllib.request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

offsets = [0, 100]
for off in offsets:
    stroka1 = 'https://api.vk.com/method/wall.get?owner_id=-29534144&count=100&v=5.73&access_token=4e4390334e4390334e439033504e21bc6044e434e4390331552d00d82502b3b1e852732&offset='+ str(off)
    req = urllib.request.Request(stroka1)
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    #print(result)
    if off == 0:
        data = json.loads(result)
    else:
        data1 = json.loads(result)
        needed_data = data1['response']['items']
        for n in needed_data:
            data['response']['items'].append(n)
#print(len(data['response']['items']))
#print(type(data))
def age_maker(a):
    a=list(a)
    if len(a)>=8:
        byear=int(''.join(a[-4:]))
        curr_age=2018-byear
        return curr_age
    else:
        pass
slovar = {}
slovar_age_comment={}
slovar_city_comment={}
f=open('post_comment.txt','w')
for m in range(199):
    f.write(data["response"]["items"][m]["text"])
    post = data["response"]["items"][m]["id"]
    for off in offsets:
        stroka = 'https://api.vk.com/method/wall.getComments?owner_id=-29534144&access_token=4e4390334e4390334e439033504e21bc6044e434e4390331552d00d82502b3b1e852732&post_id='+str(post)+'&count=100&v=5.73&extended=1&fields=bdate,city&offset='+str(off)
        requ = urllib.request.Request(stroka)
        response1 = urllib.request.urlopen(requ)
        result1 = response1.read().decode('utf-8')
        if off == 0:
            data2 = json.loads(result1)
        else:
            data3 = json.loads(result1)
            #print(data3)
            needed_data1 = data3['response']['items']
            needed_data2 = data3['response']['profiles']
            for z in needed_data1:
                data2['response']['items'].append(z)
            for c in needed_data2:
                data2['response']['profiles'].append(c)
    #print(result1)
    dlina_posta = data["response"]["items"][m]["text"]
    dlina_posta = len(dlina_posta.split())
    #print(dlina_posta)
    dlina_commentov=[]
    ids=[]
    #print(len(data2['response']['items']))
    for r in range(len(data2['response']['items'])):
        comments = data2['response']['items'][r]['text']
        ids.append(data2['response']['items'][r]['from_id'])
        f.write(comments)
        dlina_commenta = len(comments.split())
        dlina_commentov.append(dlina_commenta)
    srednyaya_dlina_commentov = sum(dlina_commentov)//len(data2['response']['items'])
    slovar[dlina_posta]=srednyaya_dlina_commentov
    cities = []
    ages = []
    for q in range(len(data2['response']['profiles'])):
        if 'city' in data2['response']['profiles'][q]:
            cities.append(data2['response']['profiles'][q]['city']['title'])
        if 'bdate' in data2['response']['profiles'][q]:
            #print(data2['response']['profiles'][q]['bdate'])
            if len(data2['response']['profiles'][q]['bdate']) >= 6:
                byear = int(''.join(data2['response']['profiles'][q]['bdate'][-4:]))
                curr_age = 2018 - byear
                ages.append(curr_age)
            else:
                pass
        #if data2['response']['profiles'][q]['id']==data2['response']['items'][q]['from_id']:
            #try:
                #print(data2['response']['profiles'][q]['city']['title'], srednyaya_dlina_commentov)
            #except KeyError:
                #pass
    #print(cities)
    #print(ages)
    dlina_commentov1=[]
    for age in ages:
        for l in range(len(data2['response']['profiles'])):
            try:
                if age_maker(data2['response']['profiles'][l]['bdate']) == age:
                    id_chel = data2['response']['profiles'][l]['id']
                    for id in ids:
                        if id==id_chel:
                            for r in range(len(data2['response']['items'])):
                                if data2['response']['items'][r]['from_id']==id:
                                    comments1 = data2['response']['items'][r]['text']
                                    dlina_commenta1=len(comments1.split())
                                    dlina_commentov1.append(dlina_commenta1)
                                    srednyaya_for_age = sum(dlina_commentov1)//len(dlina_commentov1)
                                    slovar_age_comment[age]=srednyaya_for_age
            except KeyError:
                pass
    dlina_commentov2=[]
    for city in cities:
        for k in range(len(data2['response']['profiles'])):
            try:
                if data2['response']['profiles'][k]['city']['title']==city:
                    id_chel1 = data2['response']['profiles'][k]['id']
                    for id in ids:
                        if id==id_chel1:
                            for s in range(len(data2['response']['items'])):
                                if data2['response']['items'][s]['from_id']==id:
                                    comments2 = data2['response']['items'][s]['text']
                                    dlina_commenta2=len(comments2.split())
                                    dlina_commentov2.append(dlina_commenta2)
                                    srednyaya_for_city = sum(dlina_commentov2)//len(dlina_commentov2)
                                    slovar_city_comment[city]=srednyaya_for_city
            except KeyError:
                pass
#print(slovar_age_comment)
#print(slovar_city_comment)
f.close()

#print(slovar)

import matplotlib.pyplot as plt
x = sorted(slovar.keys())
y = slovar.values()
plt.plot(x,y)
plt.title('Как соотносится длина поста с средней длиной комментариев?')
plt.xlabel('Длина поста')
plt.ylabel('Средняя длина комментариев')
plt.savefig('post_with_comments.png', dpi=100, format='png')
plt.show()
#plt.savefig('post_with_comments.png', dpi=300, format='png')

plt.plot(sorted(slovar_age_comment.keys()), slovar_age_comment.values())
plt.title('Возраст и многословность')
plt.xlabel('Возраст')
plt.ylabel('Средняя длина коммента')
plt.savefig('age_with_comments.png', dpi=100, format='png')
plt.show()
#plt.savefig('age_with_comments.png', dpi=300, format='png')

plt.bar(slovar_city_comment.keys(), slovar_city_comment.values())
plt.title('Города и многословность')
plt.xlabel('Города')
plt.ylabel('Средняя длина комментариев')
plt.xticks(range(len(slovar_city_comment.keys())), slovar_city_comment.keys(), rotation=90)
plt.savefig('city_with_comments.png', dpi=100, format='png')
plt.show()
#plt.savefig('city_with_comments.png', dpi=300, format='png')
#есть файл json data со всеми постами и информацией о них. Есть файл json data2 со всеми комментами и информацией о них, а так же о пользователях, оставивших коммент. Есть словарь slovar, где ключ - длина поста в словах, а значение - средняя длина комментов к этому посту. Есть график про длину поста и длину комментов. Есть выкачивание возраста и города для комментаторов.
#Нужно выкачать текст комметария с фром_айди = этому айди


# for q in range(len(data2['response']['profiles'])):
#     if 'city' in data2['response']['profiles'][q]:
#         print(data2['response']['profiles'][q]['city']['title'])
#     #if data2['response']['profiles'][q]['id']==data['response']['items'][q]['from_id']:
#         print(data2['response']['profiles'][q],data2['response']['items'][q])
#print(user_with_comment)


