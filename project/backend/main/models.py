import datetime

from django import forms
from djongo import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    object = models.CharField('объект', max_length=50)
    corpus = models.CharField('корпус', max_length=50)
    cabinet = models.CharField('кабинет', max_length=50)
    unit = models.CharField('подразделение', max_length=50)

    class Meta:
        abstract = True
        verbose_name = 'местонахождение'


class Component(models.Model):
    name = models.CharField('название', max_length=50, default='')
    serial_n = models.CharField('заводской номер', max_length=100, default='', unique=True)
    category = models.CharField('категория', max_length=50, default='')
    type = models.CharField('тип техники', max_length=50, default='')
    view = models.CharField('вид техники', max_length=50, default='')
    location = models.EmbeddedField(model_container=Location)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name = 'компонент'
        verbose_name_plural = 'компоненты'


class Employee(models.Model):

    surname = models.CharField('фамлия', max_length=50)
    name = models.CharField('имя', max_length=50)
    secname = models.CharField('отчество', max_length=50)

    def __str__(self):
        return self.surname + ' ' + self.name[0] + '.' + self.secname[0] + '.'

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'


class Item(models.Model):
    class otssCategoriesChoice(models.TextChoices):
        first = '1', _('1')
        second = '2', _('2')
        third = '3', _('3'),
        notSecret = '4', _('не секретно')

    class conditionsChoice(models.TextChoices):
        ok = '1', _('исправно'),
        not_ok = '2', _('неисправно')

    class inOperationChoice(models.TextChoices):
        used = '1', _('да'),
        not_used = '2', _('нет'),

    id = models.AutoField('_id', primary_key=True)
    user = models.CharField('сотрудник, которому передали мат. ценность в пользование', max_length=100, default='')
    responsible = models.CharField( 'сотрудник, ответственный за мат. ценность', max_length=100, default='')
    components = models.ArrayField(model_container=Component, null=True)
    name = models.CharField('наименование', max_length=100, default='')
    inventory_n = models.CharField('инвентарный номер', max_length=100, default='', unique=True)
    otss_category = models.CharField('категория ОТСС', max_length=100,
                                     choices=otssCategoriesChoice.choices, default='1')
    condition = models.CharField('состояние', max_length=20,
                                 default='исправно', choices=conditionsChoice.choices)
    unit_from = models.CharField('подразделение, откуда поступила мат. ценность',
                                 max_length=50, default='')
    in_operation = models.CharField('ипользуется', choices=inOperationChoice.choices, max_length=5, default='да')
    fault_document_requisites = models.CharField('документы о неисправности', max_length=100, null=True)
    date_of_receipt = models.DateField('дата поступления на учет', default=datetime.date.today)
    number_of_receipt = models.CharField('номер требования о поступлении на учет',
                                         max_length=100, default='')
    requisites = models.CharField('реквизиты книги учета мат. ценностей',
                                  default='', max_length=100)
    transfer_date = models.DateField('дата передачи во временное пользование', blank=True, null=True)
    otss_requisites = models.CharField('реквизиты документа о категории ОТСС',
                                       max_length=100, blank=True)
    spsi_requisites = models.CharField('реквизиты документа о прохождении СПСИ',
                                       max_length=100, blank=True)
    trnasfer_requisites = models.CharField('реквизиты о передаче во временное пользование',
                                           max_length=100, blank=True)
    comment = models.TextField('примечание', max_length=4000, blank=True)
    last_check = models.DateField('дата последней проверки', default=datetime.date.today)

    objects = models.DjongoManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'материальная ценность'
        verbose_name_plural = 'материальные ценности'


class ItemForm(forms.Form):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['user'] = forms.ChoiceField(
            choices=[(o.id, str(o)) for o in Employee.objects.all()]
        )


class LocationForm(forms.Form):
    class Meta:
        model = Location
        fields = '__all__'


class ComponentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ComponentForm, self).__init__(*args, **kwargs)
        self.fields['location'] = forms.ChoiceField(
            choices=[(o.id, str(o)) for o in Location.objects.all()]
        )

    class Meta:
        model = Component
        fields = '__all__'


class EmployeeForm(forms.Form):
    class Meta:
        model = Employee
        fields = '__all__'
