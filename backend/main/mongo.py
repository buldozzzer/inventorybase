import pymongo
import datetime
from bson import ObjectId

__db_conn: pymongo.database.Database = None


def set_conn(host: str, port: int, db_name: str) -> None:
    global __db_conn
    __db_conn = pymongo.MongoClient(host, port)[db_name]


def get_conn() -> pymongo.database.Database:
    global __db_conn
    if not __db_conn:
        set_conn(
            host='localhost',  # mongo
            port=27017,
            db_name='ItemsDB')
    return __db_conn
