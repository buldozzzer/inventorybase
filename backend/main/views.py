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

from rest_framework.response import Response
from rest_framework.views import APIView

from . import mongo
from .serializers import ItemSerializer


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
        item['id'] = collection.count()
        item_id = collection.insert_one(item).inserted_id
        return Response({"success": "Item '{}' created successfully"
                        .format(item_id)})
    # def post(self, request):
    #     item = request.data.get('item')
    #     serializer = ItemSerializer(data=item)
    #     if serializer.is_valid(raise_exception=True):
    #         item_saved = serializer.save()
    #     return Response({"success": "Item '{}' created successfully"
    #                     .format(item_saved.title)})
    #
    # def put(self, request, pk):
    #     saved_item = get_object_or_404(Item.objects.all(), pk=pk)
    #     data = request.data.get('item')
    #     serializer = ItemSerializer(instance=saved_item, data=data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         item_saved = serializer.save()
    #     return Response({"success": "Item '{}' updated successfully"
    #                     .format(item_saved.inventory_n)})
    #
    # def delete(self, request, pk):
    #     # Get object with this pk
    #     item = get_object_or_404(Item.objects.all(), pk=pk)
    #     item.delete()
    #     return Response({
    #         "message": "Item with id `{}` has been deleted.".format(pk)
    #     }, status=204)
    # def post(self, request, pk):
    #     request_dict = dict(request.POST)
    #     if len(request_dict) == 1:  # DELETE, only csrftoken passed
    #         item = get_object_or_404(Item.objects.all(), pk=pk)
    #         item_name = item.name
    #         item_number = item.inventory_n
    #         item.delete()
    #
    #         message = "Материлаьная ценность '%s' с инвентарным номером  %s успешно удалена."
    #         return Response({
    #             'success': message % (item_name, item_number)
    #         })
    #
    #     elif pk == 'new':  # POST
    #         serializer = ItemSerializer(data=request.data)
    #         if serializer.is_valid(raise_exception=True):
    #             new_item = serializer.save()
    #             return Response({
    #                 'success': "Материальная ценность с инвентарным номером '%s' успешно добавлена."
    #                            % new_item.inventory_n
    #             })
    #     elif pk == 'load':  # POST
    #         return Response({
    #             'success': "Материальная ценность успешно добавлена."
    #         })
    #     else:  # PUT
    #         updated_item = get_object_or_404(Item.objects.all(), pk=pk)
    #         serializer = ItemSerializer(instance=updated_item, data=request.data, partial=True)
    #         if serializer.is_valid(raise_exception=True):
    #             updated_item = serializer.save()
    #         return Response({
    #             'success': "Предмет '%s' был успешно отредактирован." % updated_item.name
    #         })
