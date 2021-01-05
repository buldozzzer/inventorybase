import datetime

from djongo import models


class Location(models.Model):
    object = models.CharField('объект', max_length=50, blank=True)
    corpus = models.CharField('корпус', max_length=50, blank=True)
    cabinet = models.CharField('кабинет', max_length=50, blank=True)
    unit = models.CharField('подразделение', max_length=50, blank=True)

    def __str__(self):
        return self.object + ' ' + self.corpus + ' ' + self.cabinet

    class Meta:
        abstract = True
        verbose_name = 'местонахождение'


class Component(models.Model):
    name = models.CharField('название', max_length=50, default='', blank=True)
    serial_n = models.CharField('заводской номер', max_length=100, default='', unique=True,
                                blank=True)
    category = models.CharField('категория', max_length=50, default='', blank=True)
    type = models.CharField('тип техники', max_length=50, default='', blank=True)
    view = models.CharField('вид техники', max_length=50, default='', blank=True)
    year = models.CharField('год выпуска', max_length=5, default='', blank=True)
    location = models.EmbeddedField(model_container=Location, blank=True)
    cost = models.CharField('цена', max_length=10, default='', blank=True)

    def __str__(self):
        return self.name + ' ' + self.serial_n

    class Meta:
        abstract = True
        verbose_name = 'компонент'
        verbose_name_plural = 'компоненты'


class Employee(models.Model):
    surname = models.CharField('фамлия', max_length=50)
    name = models.CharField('имя', max_length=50)
    secname = models.CharField('отчество', max_length=50)

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.secname

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'


class Item(models.Model):
    otssCategoriesChoice = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('Не секретно', 'Не секретно')
    ]

    conditionsChoice = [
        ('Исправно', 'Исправно'),
        ('Неисправно', 'Неисправно')
    ]

    inOperationChoice = [
        ('Используется', 'Используется'),
        ('Не используется', 'Не используется')
    ]
    user = models.CharField('сотрудник, которому передали мат. ценность в пользование',
                            max_length=100, default='',
                            blank=True)
    responsible = models.CharField('сотрудник, ответственный за мат. ценность',
                                   max_length=100, default='')
    components = models.ArrayField(model_container=Component, null=True)
    name = models.CharField('наименование', max_length=100, default='')
    inventory_n = models.CharField('инвентарный номер', max_length=100,
                                   default='', unique=True)
    otss_category = models.CharField('категория ОТСС', max_length=100,
                                     choices=otssCategoriesChoice, default='Не секретно')
    condition = models.CharField('состояние', max_length=20,
                                 default='Исправно', choices=conditionsChoice)
    unit_from = models.CharField('подразделение, откуда поступила мат. ценность',
                                 max_length=50, default='')
    in_operation = models.CharField('ипользуется', choices=inOperationChoice,
                                    max_length=20, default='да')
    fault_document_requisites = models.CharField('документы о неисправности',
                                                 max_length=100, null=True, blank=True)
    date_of_receipt = models.DateField('дата поступления на учет',
                                       default=datetime.date.today)
    number_of_receipt = models.CharField('номер требования о поступлении на учет',
                                         max_length=100, default='')
    requisites = models.TextField('реквизиты книги учета мат. ценностей',
                                  default='', max_length=4000)
    transfer_date = models.DateField('дата передачи во временное пользование',
                                     null=True, blank=True)
    otss_requisites = models.TextField('реквизиты документа о категории ОТСС',
                                       max_length=4000, blank=True)
    spsi_requisites = models.TextField('реквизиты документа о прохождении СПСИ',
                                       max_length=4000, blank=True)
    transfer_requisites = models.TextField('реквизиты о передаче во временное пользование',
                                           max_length=4000, blank=True)
    comment = models.TextField('примечание', max_length=4000, blank=True)
    last_check = models.DateField('дата последней проверки', null=True, blank=True)

    objects = models.DjongoManager()

    def __str__(self):
        return self.name.__str__()

    class Meta:
        verbose_name = 'материальная ценность'
        verbose_name_plural = 'материальные ценности'

