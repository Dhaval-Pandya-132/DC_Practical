from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time
import json
import pandas as pd
import pickle
import os
from os import path

datafiletitle='staticjs'
Metaurl ='https://s3.amazonaws.com/outagemap.duke-energy.com/data/cities/external/interval_generation_data/metadata.xml'
dataurl='https://s3.amazonaws.com/outagemap.duke-energy.com/data/cities/external/interval_generation_data/{0}/outages/{1}.js'
cities =['fl', 'in', 'ohky']
zoomin=[0,1,2,3]
title ='0320'
succeedList =[]
templist=['03200','03201','03202','03203']

html = urlopen(Metaurl.replace('cities','fl'))
html2 = dataurl.replace('cities','fl')

soup = BeautifulSoup(html, 'lxml')
metadata =soup.get_text().strip()
# html2=html2.replace('metaTag',metadata)
# html2=html2.format(metadata)
print(html2)


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list



# for k in range(0,6):
#     for i in templist :
#         for j in zoomin :
#             try :
#                 jsid= i + str(j)
#                 html3 = urlopen(html2.replace('staticjs', jsid))
#                 print(jsid + ": " + html2.replace('staticjs', jsid))
#                 succeedList.append(jsid)
#
#             except:
#                 print()
#     templist=Remove(succeedList)
#     succeedList=Remove(succeedList)

# templist=Remove(succeedList)
# succeedList=Remove(succeedList)



base = "0320"
listOfEndpoints = [base]
visitedEndpoints = set()
dataDictionary = {}
totalRequestCount = 0
successfulRequestCount = 0

while len(listOfEndpoints) > 0:

    urlBase = listOfEndpoints.pop()
    print("Processing urlBase:", urlBase)

    if urlBase in visitedEndpoints:
        print("Ignoring urlBase:", urlBase)
        continue

    listOfSuccededEndpoints = []
    for i in range(0, 4):
        totalRequestCount += 1
        print("Request no: ", totalRequestCount)
        scriptName = urlBase + str(i)
        urlToVerify = html2.format(metadata, scriptName)
        # print("New Url: ", urlToVerify)
        try :
            # response = urlopen(urlToVerify)
            response = requests.get(urlToVerify).json()
            print("URL Success", urlToVerify)
            successfulRequestCount += 1
            file_title = response["file_title"]
            file_data = response["file_data"]

            if file_title not in dataDictionary:
                dataDictionary[file_title] = file_data
            else:
                dataArray = dataDictionary[file_title]
                dataArray.append(file_data)

            listOfSuccededEndpoints.append(scriptName)
            listOfEndpoints.append(scriptName)
        except:
            print()
        time.sleep(1)

    visitedEndpoints.add(urlBase)

print("Successful requests: ", successfulRequestCount)
print("Fetched data items: ", len(dataDictionary.keys()))

for key, value in dataDictionary.items():
    print(key)


if path.exists("fetched_data.pkl") :
    os.remove("fetched_data.pkl")
f = open("fetched_data.pkl", "wb")
pickle.dump(dataDictionary,f)
f.close()


print(len(succeedList))
