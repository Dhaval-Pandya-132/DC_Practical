import time
from utils import *
from consts import *
import datetime
import database_mgr


def process_and_write_data_to_db():

    data_dictionary = get_dict_from_file(DICT_PICKLE_FILE_NAME)

    filtered_data = {}
    filtered_data_list = []

    dbconnection = database_mgr.DatabaseMgr(database_mgr.SQLITE, dbname=DATA_DB_NAME)

    for key, items in data_dictionary.items():
        print(key)
        city = str(key).split("_")[0]
        for item in items:
            if "desc" in item:
                outage_id = item["id"]
                for obj in item["desc"]:
                    if "href" in obj:
                        etr_value = obj["etr"]
                        str_value = obj["start"]
                        href_value = obj["href"]
                        href_value = href_value.replace("zoomIntoIcon", "")
                        href_value = href_value.replace("(", "")
                        href_value = href_value.replace(")", "")

                        try:
                            etr_date = datetime.datetime.strptime(etr_value, ETR_DATE_FORMAT)

                            # entry_key = str_value + "=>" + href_value
                            entry_key = str_value + "=>" + etr_value + "=>" + href_value
                            # entry_key = href_value
                            # entry_key = entry_key + href_value

                            if entry_key not in filtered_data:
                                filtered_data[entry_key] = []

                            filtered_data[entry_key].append(obj)
                            filtered_data_list.append(obj)
                        except ValueError:
                            print("ETR Date conversion failed for: ", etr_value)
                            continue

    print("Filtered Data List Count = ", len(filtered_data_list))
    print("Filtered Data Dictionary Count = ", len(filtered_data.keys()))


    idCounter = 0
    for key, value in filtered_data.items():
        # print(key, len(value))
        for item in value:
            idCounter += 1
            affected_customer = get_data_from_dict(item, DATA_JSON_KEY_CUST_A)
            max_customer_affected = get_data_from_dict(item, DATA_JSON_KEY_MAX_CUST_A)
            etr = get_data_from_dict(item,DATA_JSON_KEY_ETR)
            start = get_data_from_dict(item,DATA_JSON_KEY_START)
            crew_status = get_data_from_dict(item,DATA_JSON_KEY_CREW_STATUS)
            cause = get_data_from_dict(item,DATA_JSON_KEY_CAUSE)
            href_value = get_data_from_dict(item,DATA_JSON_KEY_HREF)


            start_date = datetime.datetime.strptime(start, ETR_DATE_FORMAT)
            start_date = start_date.replace(year=2019)
            etr_date = datetime.datetime.strptime(etr, ETR_DATE_FORMAT)
            etr_date = etr_date.replace(year=2019)

            href_value = href_value.replace("zoomIntoIcon", "")
            href_value = href_value.replace("(", "")
            href_value = href_value.replace(")", "")
            href_array = href_value.split(",")

            insert_query = []
            insert_query.append("INSERT INTO ")
            insert_query.append(DATA_TABLE_NAME)
            insert_query.append(" ")
            insert_query.append(" VALUES ")
            insert_query.append("(")
            insert_query.append(str(idCounter))
            insert_query.append(",")
            insert_query.append(affected_customer)
            insert_query.append(",")
            insert_query.append("'"+start_date.strftime(DB_DATE_FORMAT)+"'")
            insert_query.append(",")
            insert_query.append("'"+etr_date.strftime(DB_DATE_FORMAT)+"'")
            insert_query.append(",")
            insert_query.append("'"+crew_status+"'")
            insert_query.append(",")
            insert_query.append("'"+cause+"'")
            insert_query.append(",")
            insert_query.append(href_array[0])
            insert_query.append(",")
            insert_query.append(href_array[1])
            insert_query.append(",")
            insert_query.append("'"+city+"'")
            insert_query.append(")")

            insert_sql = "".join(insert_query)
            print(insert_sql)

            dbconnection.execute_query(insert_sql)

    print("Data Insertion complete...")
    dbconnection.print_all_data(DATA_TABLE_NAME)


def get_data_from_dict(dict, key, isString=True):

    result = ""

    if key in dict:
        result = dict[key]

    return result





def NES_process_and_write_data_to_db():
    data_dictionary = get_dict_from_file(NES_PICKLE_FILE_NAME)

    dbconnection = database_mgr.DatabaseMgr(database_mgr.SQLITE, dbname=DATA_DB_NAME)

    idCounter = 0
    for key, items in data_dictionary.items():
        idCounter += 1

        OutageNumber = items["OutageNumber"]
        CustAffected = items["CustAffected"]
        Long = items["X1"]
        Lat = items["Y1"]
        CrewDeployed = items["CrewDeployed"]
        OutageTime = items["OutageTime"]


        #OutageTime = datetime.datetime.strptime(OutageTime, ETR_DATE_FORMAT)
        #OutageTime = OutageTime.replace(year=2019)
        # etr_date = datetime.datetime.strptime(etr, ETR_DATE_FORMAT)
        # etr_date = etr_date.replace(year=2019)
        city2="TN"
        insert_query = []
        insert_query.append("INSERT INTO ")
        insert_query.append(DATA_TABLE_NAME)
        insert_query.append(" ")
        insert_query.append(" VALUES ")
        insert_query.append("(")
        insert_query.append(str(idCounter))
        insert_query.append(",")
        insert_query.append("'" + str(CustAffected) + "'")
        insert_query.append(",")
        insert_query.append("'" + OutageTime + "'")
        insert_query.append(",")
        insert_query.append("null")
        insert_query.append(",")
        insert_query.append("'" + str(CrewDeployed) + "'")
        insert_query.append(",")
        insert_query.append("null")
        # insert_query.append(",")
        # insert_query.append(str(OutageNumber))

        insert_query.append(",")
        insert_query.append("'" + str(Lat)+ "'")
        insert_query.append(",")
        insert_query.append("'" + str(Long)  + "'")
        insert_query.append(",")
        insert_query.append("'" + city2 + "'")

        insert_query.append(")")

        insert_sql = "".join(insert_query)
        print(insert_sql)

        dbconnection.execute_query(insert_sql)

# process_data()