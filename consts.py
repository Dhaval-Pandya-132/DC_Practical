BASE = "0320"


DICT_PICKLE_FILE_NAME = "fetched_data.pkl"
DICT_TEXT_FILE_NAME = "fetched_data.txt"
NES_PICKLE_FILE_NAME ="NESPower_DATA.pkl"
NES_TEXT_FILE_NAME ="NESPower_DATA.txt"

DATA_DB_NAME = "poweroutages.sqlite"
DATA_TABLE_NAME = 'OutageDetail'
NES_DATA_TABLE_NAME="NESOutagesDetails"


DATA_JSON_KEY_CUST_A = "cust_a"
DATA_JSON_KEY_MAX_CUST_A = "max_cust_a"
DATA_JSON_KEY_ETR = "etr"
DATA_JSON_KEY_START = "start"
DATA_JSON_KEY_CREW_STATUS = "crew_status"
DATA_JSON_KEY_CAUSE = "cause"
DATA_JSON_KEY_HREF = "href"


NES_JSON_KEY_OutageNumber = "OutageNumber"
NES_JSON_KEY_MAX_CustAffected = "CustAffected"
NES_JSON_KEY_Long = "X1"
NES_JSON_KEY_Lat = "Y1"
NES_JSON_KEY_CrewDeployed = "CrewDeployed"
NES_JSON_KEY_OutageTime = "OutageTime"
#NES_JSON_KEY_HREF = "href"







DATA_JSON_KEY_ARRAY = [DATA_JSON_KEY_CUST_A,
                       DATA_JSON_KEY_MAX_CUST_A,
                       DATA_JSON_KEY_ETR,
                       DATA_JSON_KEY_START,
                       DATA_JSON_KEY_CREW_STATUS,
                       DATA_JSON_KEY_CAUSE,
                       DATA_JSON_KEY_HREF]


ETR_DATE_FORMAT = "%b %d, %H:%M %p"

DB_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


DUKE_META_URL = 'https://s3.amazonaws.com/outagemap.duke-energy.com/data/{0}/external/interval_generation_data/metadata.xml'
DUKE_DATA_URL = 'https://s3.amazonaws.com/outagemap.duke-energy.com/data/{0}/external/interval_generation_data/{1}/outages/{2}.js'

NES_DATA_URL='https://www.nespower.com/api/outagemapdata/GetAll'
GREEN_MOUNTAIN_DATA_URL="https://api.greenmountainpower.com/api/v2/outages/incidents?active=true&format=geojson"
