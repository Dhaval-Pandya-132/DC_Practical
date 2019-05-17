from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import pandas as pd

datafiletitle='staticjs'
Metaurl ='https://s3.amazonaws.com/outagemap.duke-energy.com/data/cities/external/interval_generation_data/metadata.xml'
dataurl='https://s3.amazonaws.com/outagemap.duke-energy.com/data/cities/external/interval_generation_data/metaTag/outages/'+datafiletitle+'.js'
cities =['fl', 'in', 'ohky']
zoomin=[0,1,2,3]
title ='0320'
listofjs =[]
templist=['0320','0320','0320','0320']


html = urlopen(Metaurl.replace('cities','fl'))
html2 = dataurl.replace('cities','fl')

soup = BeautifulSoup(html, 'lxml')
#soup2 = BeautifulSoup(html2, 'lxml')
metadata =soup.get_text().strip()
html2=html2.replace('metaTag',metadata)
print(html2)



def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

def Append(datalist):
    final_list = []
    for num in datalist:
        for k in zoomin:
            final_list.append(num + str(k))
    return final_list


for i in range(0,5) :
    templist=Append(templist)


list2=Remove(templist)
print(len(templist))
print(len(list2))
print(len(templist))



for n in list2:
    try:
        html3= urlopen(html2.replace('staticjs', n))
        #html3 = urlopen('https://s3.amazonaws.com/outagemap.duke-energy.com/data/fl/external/interval_generation_data/2019_05_16_16_18_11/outages/03202.js')

        print(n + " : " + html2.replace('staticjs',n))

        #soup2 = BeautifulSoup(html2, 'lxml')
        #print(soup2.get_text())

        listofjs.append(n)
        #templist.append(title2)
        #print(title2)
    except :
        print(n)

print(len(listofjs))
#
#
# for k in range(0,10):
#   #templist=[]
#   for i in zoomin :
#     title2 = title + str(i)
#     print(title2)
#     listofjs.append(title2)
#     templist.append(title2)
#
#   for j in templist:
#     for m in zoomin :
#         print(title2)
#         listofjs.append(j+str(m))
#
#   title = title2
#
#
# listofjs=Remove(listofjs)
#
#
# for n in listofjs :
#     try:
#         html3= urlopen(html2.replace('staticjs', n))
#         #html3 = urlopen('https://s3.amazonaws.com/outagemap.duke-energy.com/data/fl/external/interval_generation_data/2019_05_16_16_18_11/outages/03202.js')
#
#         print(n + " : " + html2.replace('staticjs',n))
#
#         #soup2 = BeautifulSoup(html2, 'lxml')
#         #print(soup2.get_text())
#
#         #listofjs.append(title2)
#         #templist.append(title2)
#         #print(title2)
#     except :
#         print(n)


# for k in range(0,10):
#   templist=[]
#   for i in zoomin :
#     title2 = title + str(i)
#
#     try:
#         html3= urlopen(html2.replace('staticjs', title2))
#         #html3 = urlopen('https://s3.amazonaws.com/outagemap.duke-energy.com/data/fl/external/interval_generation_data/2019_05_16_16_18_11/outages/03202.js')
#         print(html2.replace('staticjs',title2))
#
#         #soup2 = BeautifulSoup(html2, 'lxml')
#         #print(soup2.get_text())
#
#         listofjs.append(title2)
#         templist.append(title2)
#         #print(title2)
#     except :
#         if k != 0:
#             #print(html2.replace('staticjs', title2))
#             print(title2)
#             #break
#
#   for j in templist:
#     for m in zoomin :
#         try :
#            html3 = urlopen(html2.replace('staticjs', j+str(m)))
#            print(html2.replace('staticjs', j+str(m)))
#            listofjs.append(j+str(m))
#         except :
#             print(j+str(m))
#       #print(j+str(m))
#   title = title2


print(len(listofjs))
print(listofjs)
print(templist)
#print(Metaurl.replace('cities','fl'))

# try :
#     html3 = urlopen('https://s3.amazonaws.com/outagemap.duke-energy.com/data/fl/external/interval_generation_data/2019_05_16_14_17_10/outages/032023.js')
# except:
#     print('error')


#raw_html = open('https://s3.amazonaws.com/outagemap.duke-energy.com/data/fl/external/interval_generation_data/metadata.xml?timestamp=1558011229304').read()
#print(html)

#soup = BeautifulSoup(html, 'lxml')
#soup2 = BeautifulSoup(html2, 'lxml')
#soup3 = BeautifulSoup(html3, 'lxml')

#print(soup2)
#print(type(soup2.get_text()))
#print(soup3.get_text())
#d = json.loads(soup3.get_text())
#print(d['file_data'])
#print(type((d['file_data'][0])['desc']))
#print(type(d))

#print(((d['file_data'][0])['desc'])[0])

#print(list(d)[0])

#dataList = [{'a': 1}, {'b': 3}, {'c': 5}]
#print(type(dataList))

#df=pd.DataFrame(d)
#print(pd.DataFrame(d))

#print(df['file_data'][0])
#
# for data in d['file_data']:
#     print(data)
#     for data2 in data:
#         #print(data2 + " : " + data[data2])
#         print(data[data2])
#         if data2 =='desc' :
#             for data3 in data[data2]:
#                 #print(data3)
#                 print(pd.DataFrame(data[data2]))
#                 for data4 in data3:
#
#                     print(data4 + ":" + data3[data4])





#metadata =soup.get_text()   ## Assign value to metadata which will used in URL









