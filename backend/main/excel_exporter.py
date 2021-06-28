import datetime as dt
import os
from shutil import make_archive

import pandas as pd

ALLOWED_HEADERS = {
    'name': 'Наименование',
    'user': 'Сотрудник, которому передано в пользование',
    'responsible': 'Ответственный сотрудник',
    'inventory_n': 'Инвентарный номер',
    'otss_category': 'Категория ОТСС',
    'condition': 'Сосотояние',
    'unit_from': 'Подразделение, откуда поступила мат. ценность',
    'in_operation': 'Используется',
    'fault_document_requisites': 'Документы о передаче во временное пользование',
    'date_of_receipt': 'Дата поступления на учёт',
    'number_of_receipt': 'Номер требования о поступлении на учёт',
    'requisites': 'Реквизиты книги учета мат. ценностей',
    'transfer_date': 'Дата передачи во временное пользование',
    'otss_requisites': 'Реквизиты документа о категории ОТСС',
    'spsi_requisites': 'Реквизиты документа о прохождении СПСИ',
    'transfer_requisites': 'Реквизиты документа о передаче в пользование',
    'comment': 'Примечания',
    'last_check': 'Дата последней проверки',
    'serial_n': 'Заводской номер',
    'category': 'Категория',
    'year': 'Год выпуска',
    'cost': 'Цена',
    'location_object': 'Объект',
    'location_corpus': 'Корпус',
    'location_cabinet': 'Кабинет',
    'components': 'Компоненты'
}

COMPONENT_HEADERS = {
    'id': 'Номер: ',
    'name': 'Наименование: ',
    'serial_n': 'Серийный номер: ',
    'category': 'Категория: ',
    'type': 'Тип: ',
    'year': 'Год выпуска: ',
    'cost': 'Цена: ',
    'in_operation': 'Используется: ',
    'condition': 'Состояние: ',
    'user': 'Кому передано: ',
    'location': 'Местонахождение: ',
}


def prep_data(payload):
    for item in payload:
        if '_id' in item:
            item.pop('_id')
    return True


def distribute_to_columns(payload):
    global ALLOWED_HEADERS
    global COMPONENT_HEADERS
    columns = {}
    for key in payload[0]:
        if key in payload[0]:
            columns[ALLOWED_HEADERS[key]] = []
    for key in ALLOWED_HEADERS:
        for item in payload:
            if key in item:
                if key != 'components':
                    columns[ALLOWED_HEADERS[key]] += [item[key]]
                else:
                    result_string = ''
                    for component in item['components']:
                        for header in COMPONENT_HEADERS:
                            if header != 'location':
                                result_string += COMPONENT_HEADERS[header] + \
                                                 str(component[header]) + ', '
                            else:
                                result_string += COMPONENT_HEADERS['location'] + \
                                                 'объект: ' + component['location']['object'] + ', ' + \
                                                 'корпус: ' + component['location']['corpus'] + ', ' + \
                                                 'кабинет: ' + component['location']['cabinet']
                        result_string += ';\n'
                    columns[ALLOWED_HEADERS['components']] += [result_string]
    return columns


def write(payload):
    prep_data(payload)
    prepared_data = distribute_to_columns(payload)
    filename = os.getcwd() + \
               '/media/generated/Отчёт_' + \
               dt.datetime.now().strftime('%d-%m-%Y') + '.xlsx'

    df = pd.DataFrame(prepared_data, index=[i for i in range(1, len(payload) + 1)])
    df.to_excel(filename, sheet_name='Main')
    return filename


def export_to_excel(payload: list):
    filename = write(payload)

    result_path = make_archive(os.getcwd() + '/media/Документы_' + dt.datetime.now().strftime('%d-%m-%Y'),
                               'zip',
                               root_dir=os.getcwd() + '/media/generated',
                               base_dir='.')
    return result_path
