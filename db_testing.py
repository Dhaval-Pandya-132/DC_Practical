import database_mgr
from consts import *


def main():
    dbms = database_mgr.MyDatabase(database_mgr.SQLITE, dbname=DATA_DB_NAME)

    # Create Tables
    # dbms.create_db_tables()
    dbms.create_db_tables_ForOutages()
    # dbms.insert_single_data()
    dbms.print_all_data(database_mgr.USERS)
    dbms.print_all_data(database_mgr.ADDRESSES)
    #
    # dbms.sample_query()  # simple query
    # dbms.sample_delete()  # delete data
    # dbms.sample_insert()  # insert data
    # dbms.sample_update()  # update data


# run the program
if __name__ == "__main__": main()


