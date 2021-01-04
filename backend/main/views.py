# from rest_framework.viewsets import ModelViewSet
#
# from .models import Item, Employee
# from .serializers import EmployeeSerializer, ItemSerializer
#
#
# class ItemViewSet(ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#
# class EmployeeViewSet(ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item
from .serializers import ItemSerializer


class ItemView(APIView):

    def get(self, _):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response({
            'subjects': serializer.data
        })

