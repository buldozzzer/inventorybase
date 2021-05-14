import pymongo
import os

__db_conn = None
__hostname = None
__port = None


def set_conn(host: str, port: int, db_name: str) -> None:
    global __db_conn
    global __hostname
    global __port
    __hostname = host
    __port = port
    __db_conn = pymongo.MongoClient(host, port)[db_name]


def get_conn(db_name: str = 'ItemsDB'):
    """
    :param db_name: First str parameter. Default to 'ItemsDB'
    :return: MongoClient('localhost', 27017)[`DB_NAME`]
    """

    global __db_conn
    if not __db_conn:
        set_conn(
            host=os.getenv('MONGO_HOST'),
            # host='items_db',
            # host='localhost',
            port=27017,
            db_name=db_name)
    return __db_conn


def get_param():
    return __hostname, __port
