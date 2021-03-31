import pymongo

__db_conn = None


def set_conn(host: str, port: int, db_name: str) -> None:
    global __db_conn
    __db_conn = pymongo.MongoClient(host, port)[db_name]


def get_conn(db_name: str = 'ItemsDB'):
    """
    :param db_name: First str parameter. Default to 'ItemsDB'
    :return: MongoClient('localhost', 27017)[`DB_NAME`]
    """

    global __db_conn
    if not __db_conn:
        set_conn(
            # host='items_db',
            host='localhost',
            port=27017,
            db_name=db_name)
    return __db_conn
