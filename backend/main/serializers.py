# from rest_framework import serializers
#
# from .models import employee, Location, Component, Item
#
#
# class LocationSerializer(serializers.Serializer):
#
#     object = serializers.CharField(max_length=50)
#     corpus = serializers.CharField(max_length=50)
#     cabinet = serializers.CharField(max_length=50)
#     unit = serializers.CharField(max_length=50)
#
#     def create(self, validated_data):
#         return Location.objects.create()
#
#     def update(self, instance, validated_data):
#         pass
#
#     class Meta:
#         model = Location
#         fields = "__all__"
#
#
# class ComponentSerializer(serializers.Serializer):
#
#     class Meta:
#         model = Component
#         fields = "__all__"
#
#     name = serializers.CharField(max_length=50)
#     serial_n = serializers.CharField(max_length=50)
#     category = serializers.CharField(max_length=50)
#     type = serializers.CharField(max_length=50)
#     view = serializers.CharField(max_length=50)
#     year = serializers.CharField(max_length=50)
#     cost = serializers.CharField(max_length=50)
#     location = LocationSerializer()
#
#
# class EmployeeSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = employee
#         read_only_fields = (
#             'id',
#         )
#         fields = "__all__"
#
#
# class ItemSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Item
#         fields = "__all__"
#         depth = 2
#
#     components = ComponentSerializer(many=True, allow_null=True)
#
