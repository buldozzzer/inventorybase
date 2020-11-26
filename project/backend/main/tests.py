from rest_framework import status
from rest_framework.test import APITestCase


class EmployeeTests(APITestCase):
    payload = {'surname': 'Михайлов',
               'name': 'Михаил',
               'secname': 'Иванович'}

    def test_get_employee_list(self):
        response = self.client.get('/api/v1/employee/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_add_employee(self):
        response = self.client.post('/api/v1/employee/',
                                    format='json',
                                    data=EmployeeTests.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_employee(self):
        self.client.post('/api/v1/employee/',
                         format='json',
                         data=EmployeeTests.payload)
        response = self.client.delete('/api/v1/employee/2/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_employee(self):
        self.client.post('/api/v1/employee/',
                         format='json',
                         data=EmployeeTests.payload)
        response = self.client.get('/api/v1/employee/3/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {'id': 3,
                          'surname': 'Михайлов',
                          'name': 'Михаил',
                          'secname': 'Иванович'})

    def test_put_employee(self):
        self.client.post('/api/v1/employee/',
                         format='json',
                         data=EmployeeTests.payload)
        response = self.client.get('/api/v1/employee/4/', format='json')
        self.assertEqual(response.data,
                         {'id': 4,
                          'surname': 'Михайлов',
                          'name': 'Михаил',
                          'secname': 'Иванович'})
        response = self.client.put('/api/v1/employee/4/', format='json',
                                   data={'surname': 'Степанов',
                                         'name': 'Степан',
                                         'secname': 'Степанович'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
