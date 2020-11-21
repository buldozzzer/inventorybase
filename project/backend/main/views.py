from rest_framework.viewsets import ModelViewSet

from .models import Wealth, Employee
from .serializers import EmployeeSerializer, WealthSerializer


class WealthViewSet(ModelViewSet):
    queryset = Wealth.objects.all()
    serializer_class = WealthSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



# class ComponentViewSet(ModelViewSet):
#     queryset = Component.objects.all()
#     serializer_class = ComponentSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def get(self, _):
    #     employees = Employee.objects.all()
    #     serializer = EmployeeSerializer(employees, many=True)
    #     return Response({'employees': serializer.data})
    #
    # def post(self, request):
    #     employee = request.data.get("employee")
    #     serializer = EmployeeSerializer(data=request.data)
    #     #serializer = EmployeeSerializer(data=employee)
    #     if serializer.is_valid(raise_exception=True):
    #         employee_saved = serializer.save()
    #     return Response({"success": "Employee '{}' created successfully".format(employee_saved.id)})
    #
    # def delete(self, request, pk):
    #     # Get object with this pk
    #     article = get_object_or_404(Employee.objects.all(), pk=pk)
    #     article.delete()
    #     return Response({
    #         "message": "Employee with id `{}` has been deleted.".format(pk)
    #     }, status=204)
    #
    # def put(self, request, pk):
    #     saved_employee = get_object_or_404(Employee.objects.all(), pk=pk)
    #     data = request.data.get('employee')
    #     serializer = EmployeeSerializer(instance=saved_employee, data=data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         employee_saved = serializer.save()
    #     return Response({
    #         "success": "Employee '{}' updated successfully".format(employee_saved.id)
    #     })


# {"components": [{"name":"123",
#                             "serial_n":"123",
#                             "view":"123",
#                             "type":"123",
#                             "category":"123",
#                             "location" : { "object":"123", "corpus":"123", "cabinet":"123", "unit":"123"}
#                            }, {"name":"123",
#                              "serial_n":"123",
#                              "view":"123",
#                              "type":"123",
#                              "category":"123",
#                              "location" : { "object":"123", "corpus":"123", "cabinet":"123", "unit":"123"}
#                             }],
#         "name": "123",
#         "inventory_n": "125",
#         "otss_category": "1",
#         "condition": "исправно",
#         "unit_from": "1",
#         "in_operation": "да",
#         "fault_document_requisites": "123",
#         "date_of_receipt": "1999-06-13",
#         "number_of_receipt": "123",
#         "requisites": "123",
#         "transfer_date": "1999-06-13",
#         "otss_requisites": "123",
#         "spsi_requisites": "123",
#         "trnasfer_requisites": "123",
#         "comment": "123",
#         "last_check": "1999-06-13"
# }
