# Представления для работы через Djongo
# from rest_framework.viewsets import ModelViewSet
#
# from .models import Item, employee
# from .serializers import EmployeeSerializer, ItemSerializer
#
#
# class ItemViewSet(ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#
# class EmployeeViewSet(ModelViewSet):
#     queryset = employee.objects.all()
#     serializer_class = EmployeeSerializer

from bson import ObjectId
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from . import mongo
from . import excel_exporter
from . import recognizer


def index(request):
    return render(request, 'index.html')


class ItemView(APIView):

    def get(self, _):
        """
        :param _: Default to none.
        :return: Item list. Response status 200.
        """
        result = []
        collection = mongo.get_conn()['main_item']
        items = collection.find()
        if collection:
            for document in items:
                document['_id'] = str(document['_id'])
                result.append(document)
        return Response({
            'items': result
        }, status=200)

    def post(self, request):
        """
        :param request: Request entity, contains request payload.
        :return: Response message: "message": "Item '{}' created successfully.",
                response status 201.
        """
        collection = mongo.get_conn()['main_item']
        item = request.data
        item_id = collection.insert_one(item).inserted_id
        return Response({"message": "Item '{}' created successfully."
                        .format(item_id)}, status=201)

    def delete(self, request, pk):
        """
        :param request: Request entity, contains request payload.
        :param pk: entity primary key.
        :return: Response message: "message": "Item with id `{}` has been deleted.",
                response status 204 if success, or "message": "Item with _id `{}` not found."
                response status 404 otherwise.
        """
        collection = mongo.get_conn()['main_item']
        if collection:
            collection.delete_one({"_id": ObjectId(pk)})
            return Response({"message": "Item with id `{}` has been deleted."
                            .format(pk)}, status=204)
        else:
            return Response({"message": "Item with _id `{}` not found.".format(pk)}, status=404)

    def put(self, request, pk):
        """
        :param request: Request entity, contains request payload.
        :param pk: entity primary key.
        :return: Response message: "message": "Item with id `{}` has been updated.",
                response status 202 if success, or "message": "Item with _id `{}` not found."
                response status 404 otherwise.
        """
        updated_fields = request.data
        collection = mongo.get_conn()['main_item']
        if collection:
            updated_fields.pop("_id")
            if updated_fields['components']:
                index = 1
                for component in updated_fields['components']:
                    component['id'] = index
                    index += 1
            collection.update_one({
                "_id": ObjectId(pk)
            }, {
                "$set": updated_fields
            }, upsert=False)
            return Response({"message": "Item with id `{}` has been updated."
                            .format(pk)}, status=202)
        else:
            return Response({"message": "Item with _id `{}` not found.".format(pk)}, status=404)


class EmployeeView(APIView):

    def get(self, _):
        """
            :param _: Default to none.
            :return: employee list. Response status 200.
        """
        result = []
        collection = mongo.get_conn()['main_employee']
        employees = collection.find()
        if collection:
            for document in employees:
                document['_id'] = str(document['_id'])
                result.append(document)
        return Response({
            'employees': result
        }, status=200)

    def post(self, request):
        """
            :param request: Request entity, contains request payload.
            :return: Response message: "message": "employee '{}' created successfully.",
                    response status 201.
        """
        collection = mongo.get_conn()['main_employee']
        employee = request.data
        employee_id = collection.insert_one(employee).inserted_id
        return Response({"message": "employee with _id '{}' created successfully."
                        .format(employee_id)}, status=201)

    def delete(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "employee with id `{}` has been deleted.",
                    response status 204 if success, or "message": "employee with _id `{}` not found."
                    response status 404 otherwise.
        """
        collection = mongo.get_conn()['main_employee']
        if collection:
            collection.delete_one({"_id": ObjectId(pk)})
            return Response({"message": "employee with id `{}` has been deleted."
                            .format(pk)}, status=204)
        else:
            return Response({"message": "employee with _id `{}` not found.".format(pk)}, status=404)

    def put(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "employee with id `{}` has been updated.",
                    response status 202 if success, or "message": "employee with _id `{}` not found."
                    response status 404 otherwise.
        """
        updated_fields = request.data
        collection = mongo.get_conn()['main_employee']
        if collection:
            updated_fields.pop("_id")
            collection.update_one({
                '_id': ObjectId(pk)
            }, {
                '$set': updated_fields
            }, upsert=False)
            return Response({"message": "employee with id `{}` has been updated."
                            .format(pk)}, status=202)
        else:
            return Response({"message": "employee with _id `{}` not found.".format(pk)}, status=404)


class OTSSView(APIView):

    def get(self, _):
        """
            :param _: Default to none.
            :return: OTSS category list. Response status 200.
        """
        result = []
        collection = mongo.get_conn()['main_otss']
        categories = collection.find()
        if collection:
            for document in categories:
                document['_id'] = str(document['_id'])
                result.append(document)
        return Response({
            'otss': result
        }, status=200)

    def post(self, request):
        """
            :param request: Request entity, contains request payload.
            :return: Response message: "message": "OTSS category '{}' created successfully.",
                    response status 201.
        """
        collection = mongo.get_conn()['main_otss']
        category = request.data
        category_id = collection.insert_one(category).inserted_id
        return Response({"message": "OTSS category with _id '{}' created successfully."
                        .format(category_id)}, status=201)

    def delete(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "OTSS category with id `{}` has been deleted.",
                    response status 204 if success, or "message": "OTSS category with _id `{}` not found."
                    response status 404 otherwise.
        """
        collection = mongo.get_conn()['main_otss']
        if collection:
            collection.delete_one({"_id": ObjectId(pk)})
            return Response({"message": "OTSS category with id `{}` has been deleted."
                            .format(pk)}, status=204)
        else:
            return Response({"message": "OTSS category with _id `{}` not found.".format(pk)}, status=404)

    def put(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "OTSS category with id `{}` has been updated.",
                    response status 202 if success, or "message": "OTSS category with _id `{}` not found."
                    response status 404 otherwise.
        """
        updated_fields = request.data
        collection = mongo.get_conn()['main_otss']
        if collection:
            updated_fields.pop("_id")
            collection.update_one({
                '_id': ObjectId(pk)
            }, {
                '$set': updated_fields
            }, upsert=False)
            return Response({"message": "OTSS category with id `{}` has been updated."
                            .format(pk)}, status=202)
        else:
            return Response({"message": "OTSS category with _id `{}` not found.".format(pk)}, status=404)


class UnitView(APIView):

    def get(self, _):
        """
            :param _: Default to none.
            :return: Unit list. Response status 200.
        """
        result = []
        collection = mongo.get_conn()['main_unit']
        units = collection.find()
        if collection:
            for document in units:
                document['_id'] = str(document['_id'])
                result.append(document)
        return Response({
            'units': result
        }, status=200)

    def post(self, request):
        """
            :param request: Request entity, contains request payload.
            :return: Response message: "message": "Unit '{}' created successfully.",
                    response status 201.
        """
        collection = mongo.get_conn()['main_unit']
        unit = request.data
        unit_id = collection.insert_one(unit).inserted_id
        return Response({"message": "Unit with _id '{}' created successfully."
                        .format(unit_id)}, status=201)

    def delete(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "Unit with id `{}` has been deleted.",
                    response status 204 if success, or "message": "Unit with _id `{}` not found."
                    response status 404 otherwise.
        """
        collection = mongo.get_conn()['main_unit']
        if collection:
            collection.delete_one({"_id": ObjectId(pk)})
            return Response({"message": "Unit with id `{}` has been deleted."
                            .format(pk)}, status=204)
        else:
            return Response({"message": "Unit with _id `{}` not found.".format(pk)}, status=404)

    def put(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "Unit with id `{}` has been updated.",
                    response status 202 if success, or "message": "Unit with _id `{}` not found."
                    response status 404 otherwise.
        """
        updated_fields = request.data
        collection = mongo.get_conn()['main_unit']
        if collection:
            updated_fields.pop("_id")
            collection.update_one({
                '_id': ObjectId(pk)
            }, {
                '$set': updated_fields
            }, upsert=False)
            return Response({"message": "Unit with id `{}` has been updated."
                            .format(pk)}, status=202)
        else:
            return Response({"message": "Unit with _id `{}` not found.".format(pk)}, status=404)


class TypeView(APIView):

    def get(self, _):
        """
            :param _: Default to none.
            :return: Type list. Response status 200.
        """
        result = []
        collection = mongo.get_conn()['main_type']
        types = collection.find()
        if collection:
            for document in types:
                document['_id'] = str(document['_id'])
                result.append(document)
        return Response({
            'types': result
        }, status=200)

    def post(self, request):
        """
            :param request: Request entity, contains request payload.
            :return: Response message: "message": "Type '{}' created successfully.",
                    response status 201.
        """
        collection = mongo.get_conn()['main_type']
        type = request.data
        type_id = collection.insert_one(type).inserted_id
        return Response({"message": "Type with _id '{}' created successfully."
                        .format(type_id)}, status=201)

    def delete(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "Type with id `{}` has been deleted.",
                    response status 204 if success, or "message": "Type with _id `{}` not found."
                    response status 404 otherwise.
        """
        collection = mongo.get_conn()['main_type']
        if collection:
            collection.delete_one({"_id": ObjectId(pk)})
            return Response({"message": "Type with id `{}` has been deleted."
                            .format(pk)}, status=204)
        else:
            return Response({"message": "Type with _id `{}` not found.".format(pk)}, status=404)

    def put(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "Type with id `{}` has been updated.",
                    response status 202 if success, or "message": "Type with _id `{}` not found."
                    response status 404 otherwise.
        """
        updated_fields = request.data
        collection = mongo.get_conn()['main_type']
        if collection:
            updated_fields.pop("_id")
            collection.update_one({
                '_id': ObjectId(pk)
            }, {
                '$set': updated_fields
            }, upsert=False)
            return Response({"message": "Type with id `{}` has been updated."
                            .format(pk)}, status=202)
        else:
            return Response({"message": "Type with _id `{}` not found.".format(pk)}, status=404)


class CategoryView(APIView):

    def get(self, _):
        """
            :param _: Default to none.
            :return: Category list. Response status 200.
        """
        result = []
        collection = mongo.get_conn()['main_category']
        categories = collection.find()
        if collection:
            for document in categories:
                document['_id'] = str(document['_id'])
                result.append(document)
        return Response({
            'categories': result
        }, status=200)

    def post(self, request):
        """
            :param request: Request entity, contains request payload.
            :return: Response message: "message": "Category '{}' created successfully.",
                    response status 201.
        """
        collection = mongo.get_conn()['main_category']
        category = request.data
        category_id = collection.insert_one(category).inserted_id
        return Response({"message": "Category with _id '{}' created successfully."
                        .format(category_id)}, status=201)

    def delete(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "Category with id `{}` has been deleted.",
                    response status 204 if success, or "message": "Category with _id `{}` not found."
                    response status 404 otherwise.
        """
        collection = mongo.get_conn()['main_category']
        if collection:
            collection.delete_one({"_id": ObjectId(pk)})
            return Response({"message": "Category with id `{}` has been deleted."
                            .format(pk)}, status=204)
        else:
            return Response({"message": "Category with _id `{}` not found.".format(pk)}, status=404)

    def put(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "Category with id `{}` has been updated.",
                    response status 202 if success, or "message": "Category with _id `{}` not found."
                    response status 404 otherwise.
        """
        updated_fields = request.data
        collection = mongo.get_conn()['main_category']
        if collection:
            updated_fields.pop("_id")
            collection.update_one({
                '_id': ObjectId(pk)
            }, {
                '$set': updated_fields
            }, upsert=False)
            return Response({"message": "Category with id `{}` has been updated."
                            .format(pk)}, status=202)
        else:
            return Response({"message": "Category with _id `{}` not found.".format(pk)}, status=404)


class LocationView(APIView):

    def get(self, _):
        """
            :param _: Default to none.
            :return: Location list. Response status 200.
        """
        result = []
        collection = mongo.get_conn()['main_location']
        locations = collection.find()
        if collection:
            for document in locations:
                document['_id'] = str(document['_id'])
                result.append(document)
        return Response({
            'locations': result
        }, status=200)

    def post(self, request):
        """
            :param request: Request entity, contains request payload.
            :return: Response message: "message": "Location '{}' created successfully.",
                    response status 201.
        """
        collection = mongo.get_conn()['main_location']
        location = request.data
        location_id = collection.insert_one(location).inserted_id
        return Response({"message": "Location with _id '{}' created successfully."
                        .format(location_id)}, status=201)

    def delete(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "Location with id `{}` has been deleted.",
                    response status 204 if success, or "message": "Location with _id `{}` not found."
                    response status 404 otherwise.
        """
        collection = mongo.get_conn()['main_location']
        if collection:
            collection.delete_one({"_id": ObjectId(pk)})
            return Response({"message": "Location with id `{}` has been deleted."
                            .format(pk)}, status=204)
        else:
            return Response({"message": "Location with _id `{}` not found.".format(pk)}, status=404)

    def put(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "Location with id `{}` has been updated.",
                    response status 202 if success, or "message": "Location with _id `{}` not found."
                    response status 404 otherwise.
        """
        updated_fields = request.data
        collection = mongo.get_conn()['main_location']
        if collection:
            updated_fields.pop("_id")
            collection.update_one({
                '_id': ObjectId(pk)
            }, {
                '$set': updated_fields
            }, upsert=False)
            return Response({"message": "Location with id `{}` has been updated."
                            .format(pk)}, status=202)
        else:
            return Response({"message": "Location with _id `{}` not found.".format(pk)}, status=404)


class ConditionView(APIView):

    def get(self, _):
        """
            :param _: Default to none.
            :return: Condition list. Response status 200.
        """
        result = []
        collection = mongo.get_conn()['main_condition']
        conditions = collection.find()
        if collection:
            for document in conditions:
                document['_id'] = str(document['_id'])
                result.append(document)
        return Response({
            'conditions': result
        }, status=200)

    def post(self, request):
        """
            :param request: Request entity, contains request payload.
            :return: Response message: "message": "Condition '{}' created successfully.",
                    response status 201.
        """
        collection = mongo.get_conn()['main_condition']
        condition = request.data
        condition_id = collection.insert_one(condition).inserted_id
        return Response({"message": "Condition with _id '{}' created successfully."
                        .format(condition_id)}, status=201)

    def delete(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "Condition with id `{}` has been deleted.",
                    response status 204 if success, or "message": "Condition with _id `{}` not found."
                    response status 404 otherwise.
        """
        collection = mongo.get_conn()['main_condition']
        if collection:
            collection.delete_one({"_id": ObjectId(pk)})
            return Response({"message": "Category with id `{}` has been deleted."
                            .format(pk)}, status=204)
        else:
            return Response({"message": "Category with _id `{}` not found.".format(pk)}, status=404)

    def put(self, request, pk):
        """
            :param request: Request entity, contains request payload.
            :param pk: entity primary key.
            :return: Response message: "message": "Condition with id `{}` has been updated.",
                    response status 202 if success, or "message": "Condition with _id `{}` not found."
                    response status 404 otherwise.
        """
        updated_fields = request.data
        condition = mongo.get_conn()['main_condition']
        if condition:
            updated_fields.pop("_id")
            condition.update_one({
                '_id': ObjectId(pk)
            }, {
                '$set': updated_fields
            }, upsert=False)
            return Response({"message": "Condition with id `{}` has been updated."
                            .format(pk)}, status=202)
        else:
            return Response({"message": "Condition with _id `{}` not found.".format(pk)}, status=404)


class TestView(APIView):
    def get(self, _):
        """
            :param _: Default to none.
            :return: Response status 200.
        """
        connection = mongo.get_conn()
        if connection:
            return Response({}, status=200)
        else:
            return Response({}, status=400)


class ExcelExporterView(APIView):
    def post(self, request):
        """
            :param request: Request entity, contains request payload.
            :return: Response message: "File .xlsx with name '{}' created successfully.",
                            response status 201.
        """
        payload = request.data
        filename = excel_exporter.export_to_excel(payload=payload)
        return Response({"message": "File .xlsx with name '{}' created successfully."
                        .format(filename)}, status=201)


class RecognizerView(APIView):
    def post(self, request):
        payload = request.data
        recognizer.recognizer(payload)
        return Response({"message": "SUCCESS"}, status=201)
