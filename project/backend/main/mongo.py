import shutil
from pathlib import Path
from datetime import datetime, timedelta
import pymongo
from bson import ObjectId, errors
from django.conf import settings

from backend.main.models import Wealth, Location

__db_conn: pymongo.database.Database = None


def set_conn(host: str, port: int, db_name: str) -> None:
    global __db_conn
    __db_conn = pymongo.MongoClient(host, port)[db_name]


def get_conn() -> pymongo.database.Database:
    global __db_conn
    if not __db_conn:
        set_conn(
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
            db_name=settings.DATABASES['default']['NAME'])
    return __db_conn


class MongoDB:

    _db: pymongo.database.Database
    _col: pymongo.collection.Collection

    def set_collection(self, db: pymongo.database.Database, collection_name: str) -> None:
        self._db = db
        self._col = db[collection_name]

class WealthStorage(MongoDB):

    @staticmethod
    def connect(db: pymongo.database.Database):
        storage = WealthStorage()
        storage.set_collection(
            db=db,
            collection_name='Wealth')
        return storage

    def add_one_wealth(self, item) -> None:
        self._col.insert_one(item)

    def add_many_wealth(self, items) -> None:
        self._col.insert_many(items)

    def get_one_item(self, inventory_n: str) -> dict:
        if inventory_n:
            wealth = self._col.find_one({
                'inventory_n': inventory_n
            })
        else:
            wealth = []
        return wealth

    def get_all(self) -> list:
        wealth = self._col.find()
        return list(wealth) if wealth else []

    def get_many(self, ids: list) -> list:
        items = []
        for id in ids:
            items.append(self._col.find({'inventory_n' : id}))
        return items

    def delete_by_id(self, item_id: str) -> None:

        wealth = self._col.find_one({
            '_id': ObjectId(item_id),
        })
        self._col.delete_one({
            '_id': ObjectId(item_id)
        })

    def delete_many(self, ids: list) -> int:
        delete_count = 0
        for id in ids:
            self._col.delete_one({
            '_id': ObjectId(id)
        })
            delete_count += 1
        return delete_count

    def update_component_by_serial_n(self, id: str, serial_n: str, options: list) -> None:
        self._col.find_one_and_update(
            {'_id': ObjectId(id), 'components.serial_n': serial_n},
            {'$set': {'options': options}}
        )

    def update(self, id: str, options: list) -> None:
        self._col.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set': {'options': options}}
        )

    def update_location(self, id: str, location: Location):
        self._col.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set': {'components.$[].location': location}}
        )

class EmployeeStorage(MongoDB):
    @staticmethod
    def connect(db: pymongo.database.Database):
        storage = EmployeeStorage()
        storage.set_collection(
            db=db,
            collection_name='Employee')
        return storage

    def add_one_employee(self, employee) -> None:
        self._col.insert_one(employee)

    def add_many_wealth(self, employees) -> None:
        self._col.insert_many(employees)

    def get_one_employee(self, employee_id: str) -> dict:
        if employee_id:
            employee = self._col.find_one({
                'employee_id': employee_id
            })
        else:
            employee = []
        return employee

    def get_all(self) -> list:
        employees = self._col.find()
        return list(employees) if employees else []

    def get_many(self, ids: list) -> list:
        items = []
        for id in ids:
            items.append(self._col.find({'_id': ObjectId(id)}))
        return items

    def delete_by_id(self, id: str) -> None:

        employee = self._col.find_one({
            '_id': ObjectId(id),
        })
        self._col.delete_one({
            '_id': ObjectId(id)
        })

    def delete_many(self, ids: list) -> int:
        delete_count = 0
        for id in ids:
            self._col.delete_one({
                '_id': ObjectId(id)
            })
            delete_count += 1
        return delete_count

    def update(self, id: str, options: list) -> None:
        self._col.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set': {'options': options}}
        )
