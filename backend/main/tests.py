import json
import unittest

from bson import ObjectId
from faker import Factory
from pymongo import MongoClient
from rest_framework import status
from rest_framework.test import APITestCase

from . import mongo


class BasicFunctions:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.fake = Factory.create('ru_RU')

    def generate_employee_data(self):
        fname = self.fake.first_name_male()
        fsecname = self.fake.middle_name_male()
        fsurname = self.fake.last_name_male()
        return {'surname': fsurname, 'name': fname, 'secname': fsecname}

    def import_data_from_file(self, file_name):
        data = open(file_name)
        data = json.load(data)
        return data


class TestBasicFunctions(unittest.TestCase):
    def setUp(self):
        self.mongo_functions = BasicFunctions()
        self.connection = mongo.get_conn()

    def test_generate_employee(self):
        data = self.mongo_functions.generate_employee_data()
        self.assertNotEqual(data, {})

    def test_connection(self):
        self.assertEqual(self.connection, MongoClient('localhost', 27017)['ItemsDB'])


class EmployeeTests(APITestCase):
    def setUp(self):
        self.functions = BasicFunctions()
        self.connection = mongo.get_conn()

    def test_get_employee_list(self):
        response = self.client.get('/api/v1/employee/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.connection['main_employee'].drop()

    def test_add_employee(self):
        response = self.client.post('/api/v1/employee/',
                                    format='json',
                                    data=self.functions.generate_employee_data())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.connection['main_employee'].drop()

    def test_delete_employee(self):
        self.client.post('/api/v1/employee/',
                         format='json',
                         data=self.functions.generate_employee_data())
        data_for_ids = self.client.get('/api/v1/employee/', format='json')
        _id = data_for_ids.data['employees'][0]['_id']
        response = self.client.delete('/api/v1/employee/' + _id + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.connection['main_employee'].drop()

    def test_put_employee(self):
        self.client.post('/api/v1/employee/',
                         format='json',
                         data=self.functions.generate_employee_data())
        data_for_ids = self.client.get('/api/v1/employee/', format='json')
        _id = data_for_ids.data['employees'][0]['_id']
        payload = self.functions.generate_employee_data()
        payload['_id'] = str(ObjectId(_id))
        response = self.client.put('/api/v1/employee/' + _id + '/', format='json', data=payload)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.connection['main_employee'].drop()


class ItemTests(APITestCase):

    def setUp(self):
        self.mongo_functions = BasicFunctions()
        self.connection = mongo.get_conn()
        self.form = {
            "name": self.mongo_functions.fake.name(),
            "user": self.mongo_functions.fake.name(),
            "responsible": self.mongo_functions.fake.name(),
            "components": [
                {
                    "id": 0,
                    "name": self.mongo_functions.fake.name(),
                    "serial_n": self.mongo_functions.fake.ssn(),
                    "type": self.mongo_functions.fake.ssn(),
                    "view": self.mongo_functions.fake.ssn(),
                    "category": self.mongo_functions.fake.ssn(),
                    "year": self.mongo_functions.fake.year(),
                    "cost": "1",
                    "location": {
                        "object": "1",
                        "corpus": "1",
                        "unit": "1",
                        "cabinet": "1"
                    }
                }
            ],
            "inventory_n": self.mongo_functions.fake.ssn(),
            "otss_category": "не секретно",
            "condition": "ИСправное",
            "unit_from": self.mongo_functions.fake.company_prefix(),
            "in_operation": "Используется",
            "fault_document_requisites": self.mongo_functions.fake.ssn(),
            "date_of_receipt": self.mongo_functions.fake.date(),
            "number_of_receipt": self.mongo_functions.fake.ssn(),
            "requisites": self.mongo_functions.fake.ssn(),
            "transfer_date": self.mongo_functions.fake.date(),
            "otss_requisites": self.mongo_functions.fake.ssn(),
            "spsi_requisites": self.mongo_functions.fake.ssn(),
            "transfer_requisites": self.mongo_functions.fake.ssn(),
            "comment": "COMMENT",
            "last_check": self.mongo_functions.fake.date()
        }

    def test_get_item_list(self):
        response = self.client.get('/api/v1/item/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 0)
        self.connection['main_item'].drop()

    def test_add_item(self):
        response = self.client.post('/api/v1/item/',
                                    format='json',
                                    data=self.form)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.connection['main_item'].drop()

    def test_delete_item(self):
        self.client.post('/api/v1/item/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/api/v1/item/', format='json')
        _id = data_for_ids.data['items'][0]['_id']
        response = self.client.delete('/api/v1/item/' + _id + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.connection['main_item'].drop()

    def test_put_item(self):
        self.client.post('/api/v1/item/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/api/v1/item/', format='json')
        _id = data_for_ids.data['items'][0]['_id']
        self.form['components'] = []
        self.form['_id'] = str(ObjectId(_id))
        response = self.client.put('/api/v1/item/' + _id + '/', format='json',
                                   data=self.form)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.connection['main_item'].drop()
