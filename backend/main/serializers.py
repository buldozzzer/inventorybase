from rest_framework import serializers

from .models import Employee, Location, Component, Item


class LocationSerializer(serializers.Serializer):

    class Meta:
        model = Location
        fields = "__all__"

    object = serializers.CharField(max_length=50)
    corpus = serializers.CharField(max_length=50)
    cabinet = serializers.CharField(max_length=50)
    unit = serializers.CharField(max_length=50)


class ComponentSerializer(serializers.Serializer):

    class Meta:
        model = Component
        fields = "__all__"

    name = serializers.CharField(max_length=50)
    serial_n = serializers.CharField(max_length=50)
    category = serializers.CharField(max_length=50)
    type = serializers.CharField(max_length=50)
    view = serializers.CharField(max_length=50)
    year = serializers.CharField(max_length=50)
    cost = serializers.CharField(max_length=50)
    location = LocationSerializer()


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        read_only_fields = (
            'id',
        )
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"
        depth = 2

    components = ComponentSerializer(many=True, allow_null=True)

