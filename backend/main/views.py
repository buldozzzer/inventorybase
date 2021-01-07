# Представления для работы через Djongo
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

from bson import ObjectId
from rest_framework.response import Response
from rest_framework.views import APIView

from . import mongo


class ItemView(APIView):

    def get(self, _):
        result = []
        collection = mongo.get_conn()['main_item']
        items = collection.find()
        if collection:
            number_of_items = collection.count()
            for document in items:
                document['_id'] = str(document['_id'])
                result.append(document)
        # serializer = ItemSerializer(items, many=True)
        return Response({
            'items': result, 'count': number_of_items
        })

    def post(self, request):
        collection = mongo.get_conn()['main_item']
        item = request.data
        item_id = collection.insert_one(item).inserted_id
        return Response({"message": "Item '{}' created successfully"
                        .format(item_id)})

    def delete(self, request, pk):
        collection = mongo.get_conn()['main_item']
        if collection:
            collection.delete_one({"_id": ObjectId(pk)})
            return Response({"message": "Item with id `{}` has been deleted."
                            .format(pk)}, status=204)
        else:
            Response({"message": "Item with _id `{}` not found.".format(pk)}, status=404)

    def put(self, request, pk):
        updated_fields = request.data
        collection = mongo.get_conn()['main_item']
        if collection:
            collection.update_one({
                '_id': ObjectId(pk)
            }, {
                '$set': updated_fields
            }, upsert=False)
            return Response({"message": "Item with id `{}` has been updated."
                            .format(pk)})
        else:
            Response({"message": "Item with _id `{}` not found.".format(pk)}, status=404)


class EmployeeView(APIView):

    def get(self, _):
        result = []
        collection = mongo.get_conn()['main_employee']
        employees = collection.find()
        if collection:
            number_of_items = collection.count()
            for document in employees:
                document['_id'] = str(document['_id'])
                result.append(document)
        # serializer = ItemSerializer(employees, many=True)
        return Response({
            'employees': result, 'count': number_of_items
        })

    def post(self, request):
        collection = mongo.get_conn()['main_employee']
        employee = request.data
        employee_id = collection.insert_one(employee).inserted_id
        return Response({"message": "Employee with _id '{}' created successfully"
                        .format(employee_id)})

    def delete(self, request, pk):
        collection = mongo.get_conn()['main_employee']
        if collection:
            collection.delete_one({"_id": ObjectId(pk)})
            return Response({"message": "Employee with id `{}` has been deleted."
                            .format(pk)}, status=204)
        else:
            Response({"message": "Employee with _id `{}` not found.".format(pk)}, status=404)

