from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time
# import json
# import pandas as pd
# import pickle
from consts import *


Metaurl = 'https://s3.amazonaws.com/outagemap.duke-energy.com/data/cities/external/interval_generation_data/metadata.xml'
dataurl = 'https://s3.amazonaws.com/outagemap.duke-energy.com/data/cities/external/interval_generation_data/{0}/outages/{1}.js'
cities = ['ohky','in', 'fl'] #,
zoomin = [0, 1, 2, 3]
title = '0320'
succeedList = []
templist = ['03200', '03201', '03202', '03203']

html = urlopen(Metaurl.replace('cities', 'fl'))
html2 = dataurl.replace('cities', 'fl')

soup = BeautifulSoup(html, 'lxml')
metadata = soup.get_text().strip()
# html2=html2.replace('metaTag',metadata)
# html2=html2.format(metadata)
print(html2)


def get_date_time_url_value(city_code):

    html = urlopen(DUKE_META_URL.format(city_code))
    soup = BeautifulSoup(html, 'lxml')
    metadata = soup.get_text().strip()
    return metadata


def add_response_to_dict(city, response, data_dict):

    file_title = response["file_title"]
    file_data = response["file_data"]

    key_value = city + "_" + file_title

    if key_value not in data_dict:
        data_dict[key_value] = file_data
    else:
        data_array = data_dict[key_value]
        data_array.append(file_data)


def populate_data_dict(data_dictionary):

    totalRequestCount = 0
    successfulRequestCount = 0

    for city in cities:

        listOfEndpoints = [BASE]
        visitedEndpoints = set()

        data_time_meta_value = get_date_time_url_value(city)

        while len(listOfEndpoints) > 0:

            urlBase = listOfEndpoints.pop()
            print("Processing urlBase:", urlBase)

            if urlBase in visitedEndpoints:
                print("Ignoring urlBase:", urlBase)
                continue

            listOfSuccededEndpoints = []
            for i in range(0, 4):
                totalRequestCount += 1
                scriptName = urlBase + str(i)
                urlToVerify = DUKE_DATA_URL.format(city, data_time_meta_value, scriptName)
                print("Request no: ", totalRequestCount)
                print("New Url: ", urlToVerify)

                try:
                    response = requests.get(urlToVerify).json()
                    print("URL Success", urlToVerify)
                    successfulRequestCount += 1

                    add_response_to_dict(city, response, data_dictionary)
                    listOfSuccededEndpoints.append(scriptName)
                    listOfEndpoints.append(scriptName)
                except:
                    print()
                time.sleep(0.5)

            visitedEndpoints.add(urlBase)

    print("Successful requests: ", successfulRequestCount)
    print("Fetched data items: ", len(data_dictionary.keys()))

    for key, value in data_dictionary.items():
        print(key)
