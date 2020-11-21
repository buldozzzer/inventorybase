import datetime
from djongo import models

DEFAULT_RESP_P_ID = 1


class Location(models.Model):
    object = models.CharField('объект', max_length=50)
    corpus = models.CharField('корпус', max_length=50)
    cabinet = models.CharField('кабинет', max_length=50)
    unit = models.CharField('подразделение', max_length=50)

    class Meta:
        abstract = True


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
        # verbose_name = 'компонент'
        # verbose_name_plural = 'компоненты'


class Employee(models.Model):
    GENDER_CHOICES = [
        ('М', 'М'),
        ('Ж', 'Ж')
    ]
    sirname = models.CharField('фамлия', max_length=50)
    name = models.CharField('имя', max_length=50)
    secname = models.CharField('отчество', max_length=50)
    position = models.CharField('должность', max_length=50)
    rank = models.CharField('звание', default='', max_length=50)
    gender = models.CharField('пол', max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.sirname + ' ' + self.name[0] + '.' + self.secname[0] + '.'

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'


class Wealth(models.Model):
    OTSS_CATEGORIES_CHOICE = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('не секретно', 'не секретно')
    ]
    CONDITIONS_CHOICE = [
        ('исправно', 'исправно'),
        ('неисправно', 'неисправно')
    ]
    IN_OPERATION_CHOICE = [
        ('да', 'да'),
        ('нет', 'нет')
    ]
    id = models.AutoField('_id', primary_key=True)
    user = models.ForeignKey(
        Employee,
        verbose_name='сотрудник, которому передали мат. ценность в пользование',
        related_name='employee',
        on_delete=models.DO_NOTHING)
    responsible = models.ForeignKey(
        Employee,
        verbose_name='сотрудник, ответственный за мат. ценность',
        related_name='wealth',
        on_delete=models.DO_NOTHING,
        default=DEFAULT_RESP_P_ID)
    components = models.ArrayField(model_container=Component, null=True)
    name = models.CharField('Наименование', max_length=100, default='')
    inventory_n = models.CharField('инвентарный номер', max_length=100, default='', unique=True)
    otss_category = models.CharField('категория ОТСС', max_length=100,
                                     choices=OTSS_CATEGORIES_CHOICE, default='1')
    condition = models.CharField('состояние', max_length=20,
                                 default='исправно', choices=CONDITIONS_CHOICE)
    unit_from = models.CharField('подразделение, откуда поступила мат. ценность',
                                 max_length=50, default='')
    in_operation = models.CharField('ипользуется', choices=IN_OPERATION_CHOICE, max_length=5, default='да')
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
