from consts import NES_DATA_URL
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pickle
import os
from os import path

OutageNumber = 'OutageNumber'

dataDictionary = {}


try:
    response = requests.get(NES_DATA_URL).json()
    print(type(response))
    print(response)

    for resp in response :
        if resp[OutageNumber] not in dataDictionary :
            dataDictionary[resp[OutageNumber]] = resp


except:
    print()



for key, value in dataDictionary.items():
    print(str(key) + ":" + str(value))


if path.exists("NESPower_DATA.pkl") :
    os.remove("NESPower_DATA.pkl")
f = open("NESPower_DATA.pkl", "wb")
pickle.dump(dataDictionary,f)
f.close()