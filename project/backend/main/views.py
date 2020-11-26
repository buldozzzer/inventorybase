from rest_framework.viewsets import ModelViewSet

from .models import Item, Employee
from .serializers import EmployeeSerializer, ItemSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

