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
            host='localhost',
            port=27017,
            db_name='ItemsDB')
    return __db_conn


class MongoDB:
    _db: pymongo.database.Database
    _col: pymongo.collection.Collection

    def set_collection(self, db: pymongo.database.Database, collection_name: str) -> None:
        self._db = db
        self._col = db[collection_name]


class ItemStorage(MongoDB):

    @staticmethod
    def connect(db: pymongo.database.Database):
        storage = ItemStorage()
        storage.set_collection(
            db=db,
            collection_name='main_item')
        return storage

    def insert_one(self, item) -> None:
        self._col.insert_one(item)

    def insert_many(self, items) -> None:
        self._col.insert_many(items)

    def get_one(self, item_id) -> dict:
        item = self._col.find_one({
            'id': item_id,
        })
        return item

    def get_many_by_responsible(self, responsible: str) -> list:
        items = self._col.find({
            'responsible': responsible
        })
        return list(items) if items else []

    def get_all(self) -> list:
        items = self._col.find()
        return list(items) if items else []

    def delete_by_id(self, item_id: str) -> None:
        self._col.delete_one({
            'id': item_id
        })

    def update_one(self, item_id: str,
                   user: str,
                   responsible: str,
                   components: list,
                   name: str,
                   inventory_n: str,
                   otss_category: str,
                   condition: str,
                   unit_form: str,
                   in_operation: str,
                   fault_document_requisites: str,
                   date_of_receipt: datetime.date,
                   number_of_receipt: str,
                   requisites: str,
                   transfer_date: datetime.date,
                   otss_requisites: str,
                   spsi_requisites: str,
                   transfer_requisites: str,
                   comment: str,
                   last_check: datetime.date
                   ) -> None:
        self._col.find_one_and_update(
            {'_id': ObjectId(item_id)},
            {'$set': {'user': user,
                      'responsible': responsible,
                      'components': components,
                      'name': name,
                      'inventory_n': inventory_n,
                      'otss_category': otss_category,
                      'condition': condition,
                      'unit_form': unit_form,
                      'in_operation': in_operation,
                      'fault_document_requisites': fault_document_requisites,
                      'date_of_receipt': date_of_receipt,
                      'number_of_receipt': number_of_receipt,
                      'requisites': requisites,
                      'transfer_date': transfer_date,
                      'otss_requisites': otss_requisites,
                      'spsi_requisites': spsi_requisites,
                      'transfer_requisites': transfer_requisites,
                      'comment': comment,
                      'last_check': last_check}}
        )
