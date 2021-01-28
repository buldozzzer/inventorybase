from pymongo import MongoClient
from rest_framework import status
from . import mongo
from faker import Factory
import unittest
import json
from pathlib import Path
from rest_framework.test import APITestCase


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

    def test_generate_employee(self):
        data = self.mongo_functions.generate_employee_data()
        self.assertNotEqual(data, {})

    def test_import(self):
        path = Path.cwd()
        path = str(path)
        path += '/testData/employees'
        data = self.mongo_functions.import_data_from_file(path)
        self.assertEqual(len(data), 5)
# class EmployeeTests(APITestCase):
#     payload = {'surname': 'Михайлов',
#                'name': 'Михаил',
#                'secname': 'Иванович'}
#
#
#
#     # def test_connection(self):
#
#     def test_get_employee_list(self):
#         response = self.client.get('/api/v1/employee/', format='json')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data, {
#             'employees': []
#         })

#     def test_add_employee(self):
#         response = self.client.post('/api/v1/employee/',
#                                     format='json',
#                                     data=EmployeeTests.payload)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_delete_employee(self):
#         self.client.post('/api/v1/employee/',
#                          format='json',
#                          data=EmployeeTests.payload)
#         response = self.client.delete('/api/v1/employee/2/', format='json')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#     def test_get_employee(self):
#         self.client.post('/api/v1/employee/',
#                          format='json',
#                          data=EmployeeTests.payload)
#         response = self.client.get('/api/v1/employee/3/', format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data,
#                          {'id': 3,
#                           'surname': 'Михайлов',
#                           'name': 'Михаил',
#                           'secname': 'Иванович'})
#
#     def test_put_employee(self):
#         self.client.post('/api/v1/employee/',
#                          format='json',
#                          data=EmployeeTests.payload)
#         response = self.client.get('/api/v1/employee/4/', format='json')
#         self.assertEqual(response.data,
#                          {'id': 4,
#                           'surname': 'Михайлов',
#                           'name': 'Михаил',
#                           'secname': 'Иванович'})
#         response = self.client.put('/api/v1/employee/4/', format='json',
#                                    data={'surname': 'Степанов',
#                                          'name': 'Степан',
#                                          'secname': 'Степанович'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#
# class ItemTests(APITestCase):
#     payload = {
#         'components': [
#             {
#                 'name': '123',
#                 'serial_n': '123',
#                 'category': '123',
#                 'type': '123',
#                 'view': '123',
#                 'year': '123',
#                 'location': {
#                     'object': '123',
#                     'corpus': '123',
#                     'cabinet': '123',
#                     'unit': '123'
#                 }
#             }
#         ],
#         'user': '',
#         'responsible': '---------',
#         'name': 'blablabla',
#         'inventory_n': '7737373',
#         'otss_category': 'Не секретно',
#         'condition': 'Неисправно',
#         'unit_from': 'k732',
#         'in_operation': 'Не используется',
#         'fault_document_requisites': '',
#         'date_of_receipt': '2020-11-27',
#         'number_of_receipt': '123',
#         'requisites': '123',
#         'transfer_date': '2020-11-27',
#         'otss_requisites': '123',
#         'spsi_requisites': '123',
#         'transfer_requisites': '',
#         'comment': '',
#         'last_check': '2020-11-27'
#     }
#
#     def test_get_item_list(self):
#         response = self.client.get('/api/v1/item/', format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, [])
#
#     def test_add_item(self):
#         response = self.client.post('/api/v1/item/',
#                                     format='json',
#                                     data=ItemTests.payload)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_delete_item(self):
#         self.client.post('/api/v1/item/',
#                          format='json',
#                          data=ItemTests.payload)
#         response = self.client.delete('/api/v1/item/2/', format='json')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#     def test_get_item(self):
#         self.client.post('/api/v1/item/',
#                          format='json',
#                          data=ItemTests.payload)
#         response = self.client.get('/api/v1/item/3/', format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, {
#             'id': 3,
#             'components': [
#                 {
#                     'name': '123',
#                     'serial_n': '123',
#                     'category': '123',
#                     'type': '123',
#                     'view': '123',
#                     'year': '123',
#                     'location': {
#                         'object': '123',
#                         'corpus': '123',
#                         'cabinet': '123',
#                         'unit': '123'
#                     }
#                 }
#             ],
#             'user': '',
#             'responsible': '---------',
#             'name': 'blablabla',
#             'inventory_n': '7737373',
#             'otss_category': 'Не секретно',
#             'condition': 'Неисправно',
#             'unit_from': 'k732',
#             'in_operation': 'Не используется',
#             'fault_document_requisites': '',
#             'date_of_receipt': '2020-11-27',
#             'number_of_receipt': '123',
#             'requisites': '123',
#             'transfer_date': '2020-11-27',
#             'otss_requisites': '123',
#             'spsi_requisites': '123',
#             'transfer_requisites': '',
#             'comment': '',
#             'last_check': '2020-11-27'
#         })
#
#     def test_put_item(self):
#         self.client.post('/api/v1/item/',
#                          format='json',
#                          data=ItemTests.payload)
#         response = self.client.get('/api/v1/item/4/', format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, {
#             'id': 4,
#             'components': [
#                 {
#                     'name': '123',
#                     'serial_n': '123',
#                     'category': '123',
#                     'type': '123',
#                     'view': '123',
#                     'year': '123',
#                     'location': {
#                         'object': '123',
#                         'corpus': '123',
#                         'cabinet': '123',
#                         'unit': '123'
#                     }
#                 }
#             ],
#             'user': '',
#             'responsible': '---------',
#             'name': 'blablabla',
#             'inventory_n': '7737373',
#             'otss_category': 'Не секретно',
#             'condition': 'Неисправно',
#             'unit_from': 'k732',
#             'in_operation': 'Не используется',
#             'fault_document_requisites': '',
#             'date_of_receipt': '2020-11-27',
#             'number_of_receipt': '123',
#             'requisites': '123',
#             'transfer_date': '2020-11-27',
#             'otss_requisites': '123',
#             'spsi_requisites': '123',
#             'transfer_requisites': '',
#             'comment': '',
#             'last_check': '2020-11-27'
#         })
#         response = self.client.put('/api/v1/item/4/', format='json',
#                                    data={
#                                        'components': [
#                                            {
#                                                'name': '123',
#                                                'serial_n': '123',
#                                                'category': '123',
#                                                'type': '123',
#                                                'view': '123',
#                                                'year': '123',
#                                                'location': {
#                                                    'object': '123',
#                                                    'corpus': '123',
#                                                    'cabinet': '123',
#                                                    'unit': '123'
#                                                }
#                                            }
#                                        ],
#                                        'user': '',
#                                        'responsible': 'Harry',
#                                        'name': 'blablabla',
#                                        'inventory_n': '7737373',
#                                        'otss_category': 'Не секретно',
#                                        'condition': 'Неисправно',
#                                        'unit_from': 'k732',
#                                        'in_operation': 'Не используется',
#                                        'fault_document_requisites': '',
#                                        'date_of_receipt': '2020-11-27',
#                                        'number_of_receipt': '123',
#                                        'requisites': '123',
#                                        'transfer_date': '2020-11-27',
#                                        'otss_requisites': '123',
#                                        'spsi_requisites': '123',
#                                        'transfer_requisites': '',
#                                        'comment': 'COMMENT',
#                                        'last_check': '2020-11-27'
#                                    })
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
