import pickle
from os import path
import os

dictionaryData = pickle.load(open("fetched_data.pkl", "rb"))

if path.exists("fetched_data.txt"):
    os.remove("fetched_data.txt")
txtFile = open("fetched_data.txt", "w")
txtFile.write(str(dictionaryData))
txtFile.close()


NESPower_dictionaryData = pickle.load(open("NESPower_DATA.pkl", "rb"))

if path.exists("NESPower_DATA.txt"):
    os.remove("NESPower_DATA.txt")
txtFile = open("NESPower_DATA.txt", "w")
txtFile.write(str(NESPower_dictionaryData))
txtFile.close()




for key, value in dictionaryData.items():
    print(key)