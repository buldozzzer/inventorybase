import json
import os
import unittest

from bson import ObjectId
from pymongo import MongoClient
from rest_framework import status
from rest_framework.test import APITestCase

from . import mongo, utils
from . import excel_exporter as ee


class TestConnection(unittest.TestCase):
    def setUp(self):
        self.connection = mongo.get_conn()

    def test_connection(self):
        # self.assertEqual(self.connection, MongoClient('localhost', 27017)['ItemsDB'])
        self.assertEqual(self.connection, MongoClient(os.getenv('MONGO_HOST'), 27017)['ItemsDB'])


class EmployeeTests(APITestCase):
    def setUp(self):
        self.connection = mongo.get_conn()

    def test_get_employee_list(self):
        response = self.client.get('/inventorybase/api/v1/employee/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.connection['main_employee'].drop()

    def test_add_employee(self):
        response = self.client.post('/inventorybase/api/v1/employee/',
                                    format='json',
                                    data={
                                        "name": "blablabla",
                                        "secname": "blablabla",
                                        "surname": "blablabla"
                                    })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.connection['main_employee'].drop()

    def test_delete_employee(self):
        self.client.post('/inventorybase/api/v1/employee/',
                         format='json',
                         data={
                             "name": "blablabla",
                             "secname": "blablabla",
                             "surname": "blablabla"
                         })
        data_for_ids = self.client.get('/inventorybase/api/v1/employee/', format='json')
        _id = data_for_ids.data['employees'][0]['_id']
        response = self.client.delete('/inventorybase/api/v1/employee/' + _id + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.connection['main_employee'].drop()

    def test_put_employee(self):
        self.client.post('/inventorybase/api/v1/employee/',
                         format='json',
                         data={
                             "name": "blablabla",
                             "secname": "blablabla",
                             "surname": "blablabla"
                         })
        data_for_ids = self.client.get('/inventorybase/api/v1/employee/', format='json')
        _id = data_for_ids.data['employees'][0]['_id']
        payload = {"name": "blablabla_1", "secname": "blablabla_1", "surname": "blablabla_1", '_id': str(ObjectId(_id))}
        response = self.client.put('/inventorybase/api/v1/employee/' + _id + '/', format='json', data=payload)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.connection['main_employee'].drop()


class ItemTests(APITestCase):

    def setUp(self):
        self.connection = mongo.get_conn()
        self.form = {
            "name": "blablabla",
            "user": "blablabla",
            "responsible": "blablabla",
            "components": [
                {
                    "id": 0,
                    "name": "blablabla",
                    "serial_n": "blablabla",
                    "type": "blablabla",
                    "view": "blablabla",
                    "category": "blablabla",
                    "year": "blablabla",
                    "cost": "1",
                    "location": {
                        "object": "1",
                        "corpus": "1",
                        "unit": "1",
                        "cabinet": "1"
                    }
                }
            ],
            "inventory_n": "blablabla",
            "otss_category": "не секретно",
            "condition": "Исправное",
            "unit_from": "blablabla",
            "in_operation": "Используется",
            "fault_document_requisites": "blablabla",
            "date_of_receipt": "blablabla",
            "number_of_receipt": "blablabla",
            "requisites": "blablabla",
            "transfer_date": "blablabla",
            "otss_requisites": "blablabla",
            "spsi_requisites": "blablabla",
            "transfer_requisites": "blablabla",
            "comment": "COMMENT",
            "last_check": "blablabla",
        }

    def test_get_item_list(self):
        response = self.client.get('/inventorybase/api/v1/item/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 0)
        self.connection['main_item'].drop()

    def test_add_item(self):
        response = self.client.post('/inventorybase/api/v1/item/',
                                    format='json',
                                    data=self.form)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.connection['main_item'].drop()

    def test_delete_item(self):
        self.client.post('/inventorybase/api/v1/item/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/item/', format='json')
        _id = data_for_ids.data['items'][0]['_id']
        response = self.client.delete('/inventorybase/api/v1/item/' + _id + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.connection['main_item'].drop()

    def test_put_item(self):
        self.client.post('/inventorybase/api/v1/item/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/item/', format='json')
        _id = data_for_ids.data['items'][0]['_id']
        self.form['components'] = []
        self.form['_id'] = str(ObjectId(_id))
        response = self.client.put('/inventorybase/api/v1/item/' + _id + '/', format='json',
                                   data=self.form)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.connection['main_item'].drop()


class OtssTests(APITestCase):
    def setUp(self):
        self.connection = mongo.get_conn()
        self.form = {
            'category': "blablabla",
        }

    def test_get_otss_list(self):
        response = self.client.get('/inventorybase/api/v1/otss/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.connection['main_otss'].drop()

    def test_add_otss(self):
        response = self.client.post('/inventorybase/api/v1/otss/',
                                    format='json',
                                    data=self.form)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.connection['main_otss'].drop()

    def test_delete_otss(self):
        self.client.post('/inventorybase/api/v1/otss/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/otss/', format='json')
        _id = data_for_ids.data['otss'][0]['_id']
        response = self.client.delete('/inventorybase/api/v1/otss/' + _id + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.connection['main_otss'].drop()

    def test_put_otss(self):
        self.client.post('/inventorybase/api/v1/otss/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/otss/', format='json')
        _id = data_for_ids.data['otss'][0]['_id']
        self.form['category'] = 'blablabla'
        self.form['_id'] = str(ObjectId(_id))
        response = self.client.put('/inventorybase/api/v1/otss/' + _id + '/', format='json', data=self.form)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.connection['main_otss'].drop()


class CategoryTests(APITestCase):
    def setUp(self):
        self.connection = mongo.get_conn()
        self.form = {
            'category': "blablabla",
        }

    def test_get_category_list(self):
        response = self.client.get('/inventorybase/api/v1/category/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.connection['main_category'].drop()

    def test_add_category(self):
        response = self.client.post('/inventorybase/api/v1/category/',
                                    format='json',
                                    data=self.form)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.connection['main_category'].drop()

    def test_delete_category(self):
        self.client.post('/inventorybase/api/v1/category/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/category/', format='json')
        _id = data_for_ids.data['categories'][0]['_id']
        response = self.client.delete('/inventorybase/api/v1/category/' + _id + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.connection['main_category'].drop()

    def test_put_category(self):
        self.client.post('/inventorybase/api/v1/category/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/category/', format='json')
        _id = data_for_ids.data['categories'][0]['_id']
        self.form['category'] = 'blablabla'
        self.form['_id'] = str(ObjectId(_id))
        response = self.client.put('/inventorybase/api/v1/category/' + _id + '/', format='json', data=self.form)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.connection['main_category'].drop()


class UnitTests(APITestCase):
    def setUp(self):
        self.connection = mongo.get_conn()
        self.form = {
            'units': "blablabla",
        }

    def test_get_unit_list(self):
        response = self.client.get('/inventorybase/api/v1/unit/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.connection['main_unit'].drop()

    def test_add_unit(self):
        response = self.client.post('/inventorybase/api/v1/unit/',
                                    format='json',
                                    data=self.form)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.connection['main_unit'].drop()

    def test_delete_unit(self):
        self.client.post('/inventorybase/api/v1/unit/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/unit/', format='json')
        _id = data_for_ids.data['units'][0]['_id']
        response = self.client.delete('/inventorybase/api/v1/unit/' + _id + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.connection['main_unit'].drop()

    def test_put_unit(self):
        self.client.post('/inventorybase/api/v1/unit/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/unit/', format='json')
        _id = data_for_ids.data['units'][0]['_id']
        self.form['unit'] = 'blablabla'
        self.form['_id'] = str(ObjectId(_id))
        response = self.client.put('/inventorybase/api/v1/unit/' + _id + '/', format='json', data=self.form)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.connection['main_unit'].drop()


class TypeTests(APITestCase):
    def setUp(self):
        self.connection = mongo.get_conn()
        self.form = {
            'types': "blablabla",
        }

    def test_get_type_list(self):
        response = self.client.get('/inventorybase/api/v1/type/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.connection['main_type'].drop()

    def test_add_type(self):
        response = self.client.post('/inventorybase/api/v1/type/',
                                    format='json',
                                    data=self.form)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.connection['main_type'].drop()

    def test_delete_type(self):
        self.client.post('/inventorybase/api/v1/type/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/type/', format='json')
        _id = data_for_ids.data['types'][0]['_id']
        response = self.client.delete('/inventorybase/api/v1/type/' + _id + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.connection['main_type'].drop()

    def test_put_type(self):
        self.client.post('/inventorybase/api/v1/type/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/type/', format='json')
        _id = data_for_ids.data['types'][0]['_id']
        self.form['type'] = 'blablabla'
        self.form['_id'] = str(ObjectId(_id))
        response = self.client.put('/inventorybase/api/v1/type/' + _id + '/', format='json', data=self.form)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.connection['main_type'].drop()


class LocationsTests(APITestCase):
    def setUp(self):
        self.connection = mongo.get_conn()
        self.form = {
            "object": "blablabla",
            "corpus": "blablabla",
            "unit": "blablabla",
            "cabinet": "blablabla",
        }

    def test_get_location_list(self):
        response = self.client.get('/inventorybase/api/v1/location/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.connection['main_location'].drop()

    def test_add_location(self):
        response = self.client.post('/inventorybase/api/v1/location/',
                                    format='json',
                                    data=self.form)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.connection['main_location'].drop()

    def test_delete_location(self):
        self.client.post('/inventorybase/api/v1/location/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/location/', format='json')
        _id = data_for_ids.data['locations'][0]['_id']
        response = self.client.delete('/inventorybase/api/v1/location/' + _id + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.connection['main_location'].drop()

    def test_put_location(self):
        self.client.post('/inventorybase/api/v1/location/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/location/', format='json')
        _id = data_for_ids.data['locations'][0]['_id']
        self.form['object'] = 'blablabla'
        self.form['_id'] = str(ObjectId(_id))
        response = self.client.put('/inventorybase/api/v1/location/' + _id + '/', format='json', data=self.form)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.connection['main_location'].drop()


class ConditionTests(APITestCase):
    def setUp(self):
        self.connection = mongo.get_conn()
        self.form = {
            'conditions': "blablabla",
        }

    def test_get_type_list(self):
        response = self.client.get('/inventorybase/api/v1/condition/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.connection['main_condition'].drop()

    def test_add_type(self):
        response = self.client.post('/inventorybase/api/v1/condition/',
                                    format='json',
                                    data=self.form)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.connection['main_condition'].drop()

    def test_delete_type(self):
        self.client.post('/inventorybase/api/v1/condition/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/condition/', format='json')
        _id = data_for_ids.data['conditions'][0]['_id']
        response = self.client.delete('/inventorybase/api/v1/condition/' + _id + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.connection['main_condition'].drop()

    def test_put_type(self):
        self.client.post('/inventorybase/api/v1/condition/',
                         format='json',
                         data=self.form)
        data_for_ids = self.client.get('/inventorybase/api/v1/condition/', format='json')
        _id = data_for_ids.data['conditions'][0]['_id']
        self.form['condition'] = 'blablabla'
        self.form['_id'] = str(ObjectId(_id))
        response = self.client.put('/inventorybase/api/v1/condition/' + _id + '/', format='json', data=self.form)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.connection['main_condition'].drop()


class ExcelExporterTests(APITestCase):
    def setUp(self) -> None:
        self.payload = [
            {
                'name': 'name_1',
                'user': 'test_user',
                'responsible': 'test_responsible',
                'components': [{
                    'name': 'comp_name1_sample1',
                    'serial_n': 'comp_serial_n_sample1',
                    'type': 'comp_type_sample1',
                    'view': 'comp_view_sample1',
                    'category': 'comp_category_sample1',
                    'year': 'comp_year_sample1',
                    'cost': 'comp_cost_sample1',
                    'location': {
                        'object': 'comp_object_sample1',
                        'corpus': 'comp_corpus_sample1',
                        'unit': 'comp_unit_sample1',
                        'cabinet': 'comp_cabinet_sample1',
                    },
                    'in_operation': '+',
                    'condition': '+',
                    'user': '+'
                },
                    {
                        'name': 'comp_name2_sample1',
                        'serial_n': 'comp_serial_n_sample1',
                        'type': 'comp_type_sample1',
                        'view': 'comp_view_sample1',
                        'category': 'comp_category_sample1',
                        'year': 'comp_year_sample1',
                        'cost': 'comp_cost_sample1',
                        'location': {
                            'object': 'comp_object_sample1',
                            'corpus': 'comp_corpus_sample1',
                            'unit': 'comp_unit_sample1',
                            'cabinet': 'comp_cabinet_sample1',
                        },
                        'in_operation': '+',
                        'condition': '+',
                        'user': '+'
                    }],
                'inventory_n': 'test_inventory_n',
                'otss_category': 'test_otss_category',
                'condition': 'test_condition',
                'unit_from': 'test_unit_from',
                'in_operation': 'test_in_operation',
                'fault_document_requisites': 'test_fault_document_requisites',
                'date_of_receipt': 'test_date_of_receipt',
                'number_of_receipt': 'test_number_of_receipt',
                'requisites': 'test_requisites',
                'transfer_date': 'test_transfer_date',
                'otss_requisites': 'test_otss_requisites',
                'spsi_requisites': 'test_spsi_requisites',
                'transfer_requisites': 'test_transfer_requisites',
                'comment': 'test_comment',
                'last_check': 'test_last_check',
            },
            {
                'name': 'name_2',
                'user': 'test_user',
                'responsible': '',
                'components': [],
                'inventory_n': 'test_inventory_n',
                'otss_category': 'test_otss_category',
                'condition': 'test_condition',
                'unit_from': 'test_unit_from',
                'in_operation': 'test_in_operation',
                'fault_document_requisites': 'test_fault_document_requisites',
                'date_of_receipt': 'test_date_of_receipt',
                'number_of_receipt': 'test_number_of_receipt',
                'requisites': 'test_requisites',
                'transfer_date': 'test_transfer_date',
                'otss_requisites': 'test_otss_requisites',
                'spsi_requisites': 'test_spsi_requisites',
                'transfer_requisites': 'test_transfer_requisites',
                'comment': 'test_comment',
                'last_check': 'test_last_check',
            },
            {
                'name': 'name_3',
                'user': 'test_user',
                'responsible': 'test_responsible',
                'components': [{
                    'name': 'comp_name_sample2',
                    'serial_n': 'comp_serial_n_sample2',
                    'type': 'comp_type_sample2',
                    'view': 'comp_view_sample2',
                    'category': 'comp_category_sample2',
                    'year': 'comp_year_sample2',
                    'cost': 'comp_cost_sample2',
                    'location': {
                        'object': 'comp_object_sample2',
                        'corpus': 'comp_corpus_sample2',
                        'unit': 'comp_unit_sample2',
                        'cabinet': 'comp_cabinet_sample2',
                    },
                    'in_operation': '+',
                    'condition': '+',
                    'user': '+'
                }],
                'inventory_n': 'test_inventory_n',
                'otss_category': 'test_otss_category',
                'condition': 'test_condition',
                'unit_from': 'test_unit_from',
                'in_operation': 'test_in_operation',
                'fault_document_requisites': 'test_fault_document_requisites',
                'date_of_receipt': 'test_date_of_receipt',
                'number_of_receipt': 'test_number_of_receipt',
                'requisites': 'test_requisites',
                'transfer_date': 'test_transfer_date',
                'otss_requisites': 'test_otss_requisites',
                'spsi_requisites': 'test_spsi_requisites',
                'transfer_requisites': 'test_transfer_requisites',
                'comment': 'test_comment',
                'last_check': 'test_last_check',
            },
        ]

    def test_get_nested_components(self):
        my_nested_components = {('Компоненты', 'Наименование'): {(1, 1): 'comp_name1_sample1',
                                                                 (1, 2): 'comp_name2_sample1',
                                                                 (3, 1): 'comp_name_sample2'},
                                ('Компоненты', 'Серийный номер'): {(1, 1): 'comp_serial_n_sample1',
                                                                   (1, 2): 'comp_serial_n_sample1',
                                                                   (3, 1): 'comp_serial_n_sample2'},
                                ('Компоненты', 'Тип'): {(1, 1): 'comp_type_sample1',
                                                        (1, 2): 'comp_type_sample1',
                                                        (3, 1): 'comp_type_sample2'},
                                ('Компоненты', 'Категория'): {(1, 1): 'comp_category_sample1',
                                                              (1, 2): 'comp_category_sample1',
                                                              (3, 1): 'comp_category_sample2'},
                                ('Компоненты', 'Год выпуска'): {(1, 1): 'comp_year_sample1',
                                                                (1, 2): 'comp_year_sample1',
                                                                (3, 1): 'comp_year_sample2'},
                                ('Компоненты', 'Цена'): {(1, 1): 'comp_cost_sample1',
                                                         (1, 2): 'comp_cost_sample1',
                                                         (3, 1): 'comp_cost_sample2'},
                                ('Компоненты',
                                 'Местонахождение'): {(1, 1): 'Объект: comp_object_sample1,\nкорпус: '
                                                              'comp_corpus_sample1,\nкабинет: comp_cabinet_sample1',
                                                      (1, 2): 'Объект: comp_object_sample1,\nкорпус: '
                                                              'comp_corpus_sample1,\nкабинет: comp_cabinet_sample1',
                                                      (3, 1): 'Объект: comp_object_sample2,\nкорпус: '
                                                              'comp_corpus_sample2,\nкабинет: comp_cabinet_sample2'},
                                ('Компоненты',
                                 'Используется?'): {(1, 1): '+',
                                                    (1, 2): '+',
                                                    (3, 1): '+'},
                                ('Компоненты', 'Состояние'): {
                                    (1, 1): '+',
                                    (1, 2): '+',
                                    (3, 1): '+'},
                                ('Компоненты', 'Кому передано в пользование'): {
                                    (1, 1): '+',
                                    (1, 2): '+',
                                    (3, 1): '+'}
                                }
        self.maxDiff = None
        self.assertEqual(my_nested_components, ee.get_nested_components(self.payload))

    def test_get_items(self):
        self.assertEqual(len(self.payload[0]) - 1, len(ee.get_items(self.payload)))

    def test_get_indices(self):
        nested_components = ee.get_nested_components(self.payload)
        items = ee.get_items(self.payload)
        merge_data = {**items, **nested_components}
        self.assertEqual([(1, 1),
                          (1, 2),
                          (2, 1),
                          (3, 1)], list(ee.get_indices(merge_data)))

    def test_get_indices_without_nested_components(self):
        items = ee.get_items(self.payload)
        merge_data = {**items, **{}}
        self.assertEqual([(1, 1),
                          (2, 1),
                          (3, 1)], list(ee.get_indices(merge_data)))

    def test_export_to_excel(self):
        self.assertNotEqual(None, ee.export_to_excel(self.payload))


class TestConnectionTests(APITestCase):

    def test_get_type_list(self):
        response = self.client.get('/inventorybase/api/v1/test/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UtilsTests(unittest.TestCase):
    def setUp(self):
        self.item = {
                'name': '           name_1          ',
                'user': '   test_user',
                'responsible': '            test_responsible            ',
                'components': [{
                    'name': 'comp_name1_sample1',
                    'serial_n': 'comp_serial_n_sample1',
                    'type': 'comp_type_sample1',
                    'view': 'comp_view_sample1',
                    'category': 'comp_category_sample1',
                    'year': 'comp_year_sample1',
                    'cost': 'comp_cost_sample1',
                    'location': {
                        'object': 'comp_object_sample1',
                        'corpus': 'comp_corpus_sample1',
                        'unit': 'comp_unit_sample1',
                        'cabinet': 'comp_cabinet_sample1',
                    },
                    'in_operation': '                   ',
                    'condition': '+',
                    'user': '+'
                },
                    {
                        'name': 'comp_name2_sample1',
                        'serial_n': 'comp_serial_n_sample1',
                        'type': 'comp_type_sample1',
                        'view': 'comp_view_sample1',
                        'category': 'comp_category_sample1',
                        'year': 'comp_year_sample1',
                        'cost': 'comp_cost_sample1',
                        'location': {
                            'object': 'comp_object_sample1',
                            'corpus': 'comp_corpus_sample1',
                            'unit': 'comp_unit_sample1',
                            'cabinet': 'comp_cabinet_sample1',
                        },
                        'in_operation': '+',
                        'condition': '+',
                        'user': '+'
                    }],
                'inventory_n': '    test_inventory_n',
                'otss_category': 'test_otss_category',
                'condition': ' test_condition  ',
                'unit_from': '  test_unit_from  ',
                'in_operation': 'test_in_operation',
                'fault_document_requisites': ' test_fault_document_requisites',
                'date_of_receipt': 'test_date_of_receipt',
                'number_of_receipt': 'test_number_of_receipt',
                'requisites': 'test_requisites      ',
                'transfer_date': 'test_transfer_date    ',
                'otss_requisites': '    test_otss_requisites',
                'spsi_requisites': 'test_spsi_requisites',
                'transfer_requisites': 'test_transfer_requisites',
                'comment': 'test_comment',
                'last_check': 'test_last_check',
            }
        self.data_to_encode = [{'inventory_n': 'blablabla',
                                   'serial_n': 'blablabla'}]

    def test_strip(self):
        final_item = {
                'name': 'name_1',
                'user': 'test_user',
                'responsible': 'test_responsible',
                'components': [{
                    'name': 'comp_name1_sample1',
                    'serial_n': 'comp_serial_n_sample1',
                    'type': 'comp_type_sample1',
                    'view': 'comp_view_sample1',
                    'category': 'comp_category_sample1',
                    'year': 'comp_year_sample1',
                    'cost': 'comp_cost_sample1',
                    'location': {
                        'object': 'comp_object_sample1',
                        'corpus': 'comp_corpus_sample1',
                        'unit': 'comp_unit_sample1',
                        'cabinet': 'comp_cabinet_sample1',
                    },
                    'in_operation': '',
                    'condition': '+',
                    'user': '+'
                },
                    {
                        'name': 'comp_name2_sample1',
                        'serial_n': 'comp_serial_n_sample1',
                        'type': 'comp_type_sample1',
                        'view': 'comp_view_sample1',
                        'category': 'comp_category_sample1',
                        'year': 'comp_year_sample1',
                        'cost': 'comp_cost_sample1',
                        'location': {
                            'object': 'comp_object_sample1',
                            'corpus': 'comp_corpus_sample1',
                            'unit': 'comp_unit_sample1',
                            'cabinet': 'comp_cabinet_sample1',
                        },
                        'in_operation': '+',
                        'condition': '+',
                        'user': '+'
                    }],
                'inventory_n': 'test_inventory_n',
                'otss_category': 'test_otss_category',
                'condition': 'test_condition',
                'unit_from': 'test_unit_from',
                'in_operation': 'test_in_operation',
                'fault_document_requisites': 'test_fault_document_requisites',
                'date_of_receipt': 'test_date_of_receipt',
                'number_of_receipt': 'test_number_of_receipt',
                'requisites': 'test_requisites',
                'transfer_date': 'test_transfer_date',
                'otss_requisites': 'test_otss_requisites',
                'spsi_requisites': 'test_spsi_requisites',
                'transfer_requisites': 'test_transfer_requisites',
                'comment': 'test_comment',
                'last_check': 'test_last_check',
            }
        self.assertEqual(final_item, utils.prepare_data(self.item))

    def test_datamatrix_output_docx_file(self):
        utils.create_data_matrix(self.data_to_encode)
        self.assertEqual(True, os.path.isfile(os.getcwd() + '/media/Коды.docx'))

    def test_datamatrix_generated_png_file(self):
        utils.create_data_matrix(self.data_to_encode)
        self.assertEqual(True, os.path.isfile(os.getcwd() + '/media/codes/inv:blablabla ser:blablabla.png'))

    def delete_all_files(self):
        utils.create_data_matrix(self.data_to_encode)
        utils.del_all('/media/codes/', '*.png')
        self.assertEqual([], os.listdir(os.getcwd() + '/media/codes/'))

