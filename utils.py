import pickle
from os import path
import os
def get_dict_from_file(file_name):
    dictionary_data = pickle.load(open(file_name, "rb"))
    return dictionary_data


def write_dict_to_file(file_name):
    dictionary_data = get_dict_from_file(file_name)
    txtFile = open(file_name, "w")
    txtFile.write(str(dictionary_data))
    txtFile.close()


def write_dict_to_pickle_file(data_dict, file_name):
    if path.exists(file_name) :
        os.remove(file_name)
    f = open(file_name, "wb")
    pickle.dump(data_dict, f)
    f.close()

