from consts import *
from utils import *
import scrape_data
import process_data


def main():

    data_dictionary = {}

    scrape_data.populate_data_dict(data_dictionary)
    write_dict_to_pickle_file(data_dictionary, DICT_PICKLE_FILE_NAME)
    process_data.process_and_write_data_to_db()
    process_data.NES_process_and_write_data_to_db()

# run the program
if __name__ == "__main__": main()
