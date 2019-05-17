from sqlalchemy import create_engine
from consts import *

# Global Variables
SQLITE = 'sqlite'


"""
CREATE Table OutageDetail

(
ID interger identity(1,1) PRIMARY KEY  ,
 Affected_Customer Integer,
 StartDate DATETIME,
 ETR DateTime,
 Crew_status  Varhcar(100),
 Cause Varhcar(100),
 Lat  FLOAT,
 Long  FLOAT

)
"""


class DatabaseMgr:

    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: 'sqlite:///{0}'.format(DATA_DB_NAME)
    }

    # Main DB Connection Ref Obj
    db_engine = None

    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in DB_ENGINE")

    # Insert, Update, Delete
    def execute_query(self, query=''):
        if query == '': return
        print(query)

        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def print_all_data(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print(query)

        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row)  # print(row[0], row[1], row[2])
                result.close()
                print("\n")
