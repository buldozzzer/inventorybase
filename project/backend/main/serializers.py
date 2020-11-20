from rest_framework import serializers
from rest_framework_mongoengine.fields import ObjectIdField

from .models import Employee, Location, Component, Wealth


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
        #fields = ('name', 'serial_n', 'category', 'type', 'view', 'location', 'wealth')
    name = serializers.CharField(max_length=50)
    serial_n = serializers.CharField(max_length=50)
    category = serializers.CharField(max_length=50)
    type = serializers.CharField(max_length=50)
    view = serializers.CharField(max_length=50)
    location = LocationSerializer()


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        read_only_fields = (
            'id',
        )
        fields = "__all__"
    # id = serializers.ReadOnlyField()
    # sirname = serializers.CharField(max_length=50)
    # name = serializers.CharField(max_length=50)
    # secname = serializers.CharField(max_length=50)
    # position = serializers.CharField(max_length=50)
    # rank = serializers.CharField(max_length=50)
    # gender = serializers.CharField(max_length=50)
    #
    # def update(self, instance, validated_data):
    #     instance.sirname = validated_data.get('sirname', instance.sirname)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.secname = validated_data.get('secname', instance.secname)
    #     instance.position = validated_data.get('position', instance.position)
    #     instance.rank = validated_data.get('rank', instance.rank)
    #     instance.gender = validated_data.get('gender', instance.gender)
    #     instance.save()
    #     return instance
    #
    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data)


class WealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wealth
        fields = "__all__"
        depth = 2
    components = ComponentSerializer(many=True, allow_null=True)
    # id = serializers.ReadOnlyField()
    # name = serializers.CharField(max_length=50)
    # user = EmployeeSerializer()
    # responsible = EmployeeSerializer()
    # components = ComponentSerializer(many=True)
    # inventory_n = serializers.CharField(max_length=50)
    # otss_category = serializers.CharField(max_length=50)
    # condition = serializers.CharField(max_length=50)
    # unit_from = serializers.CharField(max_length=50)
    # in_operation = serializers.CharField(max_length=50)
    # fault_document_requisites = serializers.CharField(max_length=50)
    # date_of_receipt = serializers.DateField()
    # number_of_receipt = serializers.CharField(max_length=50)
    # requisites = serializers.CharField(max_length=50)
    # transfer_date = serializers.DateField()
    # otss_requisites = serializers.CharField(max_length=50)
    # spsi_requisites = serializers.CharField(max_length=50)
    # trnasfer_requisites = serializers.CharField(max_length=50)
    # comment = serializers.CharField()
    # last_check = serializers.DateField()
