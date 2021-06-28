import datetime as dt
import os
from pathlib import Path
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
}


def get_nested_components(payload: list):
    """
    This method extracts information about nested components
    and forms dict of dicts in which key is pair of item index
    and number of item`s nested component
    :param payload: item list
    :return: return list of nested components
    """
    nested_components = {
        ('Компоненты', 'Наименование'): {},
        ('Компоненты', 'Серийный номер'): {}, ('Компоненты', 'Тип'): {},
        ('Компоненты', 'Категория'): {}, ('Компоненты', 'Год выпуска'): {},
        ('Компоненты', 'Цена'): {}, ('Компоненты', 'Местонахождение'): {},
        ('Компоненты', 'Используется?'): {}, ('Компоненты', 'Состояние'): {},
        ('Компоненты', 'Кому передано в пользование'): {},
    }

    component_titles = ['name', 'serial_n', 'type',
                        'category', 'year', 'cost',
                        'location', 'in_operation', 'condition', 'user']

    for key, title in zip(component_titles, nested_components):
        component_cell = {}
        for i in range(len(payload)):
            for j in range(len(payload[i]['components'])):
                component_cell[(i + 1, j + 1)] = payload[i]['components'][j][key]
        nested_components[title] = component_cell

    for sample in nested_components[('Компоненты', 'Местонахождение')]:
        nested_components[('Компоненты', 'Местонахождение')][sample] = \
            'Объект: ' + nested_components[('Компоненты', 'Местонахождение')][sample]['object'] + \
            ',\nкорпус: ' + nested_components[('Компоненты', 'Местонахождение')][sample]['corpus'] + \
            ',\nкабинет: ' + nested_components[('Компоненты', 'Местонахождение')][sample]['cabinet']

    return nested_components


def get_items(payload: list):
    """
    :param payload: item list
    :return: dict of items without nested components
    """
    item_dict = {}
    item_titles = []

    for key in payload[0].keys():
        if 'name' == key:
            item_dict[('', 'Наименование')] = {}
            item_titles.append(key)
        if 'responsible' == key:
            item_dict[('', 'Ответственный сотрудник')] = {}
            item_titles.append(key)
        if 'inventory_n' == key:
            item_dict[('', 'Инвентарный номер')] = {}
            item_titles.append(key)
        if 'otss_category' == key:
            item_dict[('', 'Категория ОТСС')] = {}
            item_titles.append(key)
        if 'condition' == key:
            item_dict[('', 'Состояние')] = {}
            item_titles.append(key)
        if 'unit_from' == key:
            item_dict[('', 'Подразделение, откуда поступила мат. ценность')] = {}
            item_titles.append(key)
        if 'in_operation' == key:
            item_dict[('', 'Используется?')] = {}
            item_titles.append(key)
        if 'fault_document_requisites' == key:
            item_dict[('', 'Документы о неисправности')] = {}
            item_titles.append(key)
        if 'date_of_receipt' == key:
            item_dict[('', 'Дата_поступления на учет')] = {}
            item_titles.append(key)
        if 'number_of_receipt' == key:
            item_dict[('', 'Номер требования о поступлении на учет')] = {}
            item_titles.append(key)
        if 'requisites' == key:
            item_dict[('', 'Реквизиты книги учета мат. ценностей')] = {}
            item_titles.append(key)
        if 'transfer_date' == key:
            item_dict[('', 'Дата передачи во временное пользование')] = {}
            item_titles.append(key)
        if 'otss_requisites' == key:
            item_dict[('', 'Реквизиты документа о категории ОТСС')] = {}
            item_titles.append(key)
        if 'spsi_requisites' == key:
            item_dict[('', 'Реквизиты документа о прохождении СПСИ')] = {}
            item_titles.append(key)
        if 'transfer_requisites' == key:
            item_dict[('', 'Реквизиты о передаче в пользование')] = {}
            item_titles.append(key)
        if 'last_check' == key:
            item_dict[('', 'Дата последней проверки')] = {}
            item_titles.append(key)
        if 'comment' == key:
            item_dict[('', 'Примечания')] = {}
            item_titles.append(key)
        if 'user' == key:
            item_dict[('', 'Сотрудник, которому передали в пользование')] = {}
            item_titles.append(key)
        if 'serial_n' == key:
            item_dict[('', 'Заводской номер')] = {}
            item_titles.append(key)
        if 'category' == key:
            item_dict[('', 'Категория')] = {}
            item_titles.append(key)
        if 'year' == key:
            item_dict[('', 'Год выпуска')] = {}
            item_titles.append(key)
        if 'cost' == key:
            item_dict[('', 'Цена')] = {}
            item_titles.append(key)
        if 'location_object' == key:
            item_dict[('', 'Объект')] = {}
            item_titles.append(key)
        if 'location_unit' == key:
            item_dict[('', 'Подразделение')] = {}
            item_titles.append(key)
        if 'location_corpus' == key:
            item_dict[('', 'Корпус')] = {}
            item_titles.append(key)
        if 'location_cabinet' == key:
            item_dict[('', 'Кабинет')] = {}
            item_titles.append(key)

    for ru_title, en_title in zip(item_dict, item_titles):
        temp_dict = {}
        for i in range(len(payload)):
            temp_dict[(i + 1, 1)] = payload[i][en_title]
        item_dict[ru_title] = temp_dict

    return item_dict


def get_indices(merge_df: dict):
    """
    :param merge_df: merged dict of items and their nested components
    :return: multiindex for items and their nested components
    """
    arrays = [[], []]

    for key in merge_df[('', 'Наименование')]:
        arrays[0].append(key[0])
        arrays[1].append(key[1])

    if ('Компоненты', 'Наименование') in merge_df:
        tuples = list(zip(*arrays))
        for key in merge_df[('Компоненты', 'Наименование')]:
            if key not in tuples:
                arrays[0].append(key[0])
                arrays[1].append(key[1])

    else:
        tuples = list(zip(*arrays))
        for key in merge_df:
            for multiindex in merge_df[key]:
                if multiindex not in tuples:
                    arrays[0].append(multiindex[0])
                    arrays[1].append(multiindex[1])

    tuples = list(zip(*arrays))
    tuples.sort(key=lambda key: key[0])

    index = pd.MultiIndex.from_tuples(tuples, names=[None, None])

    return index


def prep_data(payload):
    for item in payload:
        if 'components' in item:
            item.pop('components')
        if '_id' in item:
            item.pop('_id')
    return True


def distribute_to_columns(payload):
    global ALLOWED_HEADERS
    columns = {}
    for key in payload[0]:
        if key in payload[0]:
            columns[ALLOWED_HEADERS[key]] = []
    for key in ALLOWED_HEADERS:
        for item in payload:
            if key in item:
                columns[ALLOWED_HEADERS[key]] += [item[key]]
    return columns


def change_headers(payload):
    global ALLOWED_HEADERS
    prepared_data = []
    for item in payload:
        prepared_item = {}
        for key in item:
            prepared_item[ALLOWED_HEADERS[key]] = item[key]
        prepared_data += [prepared_item]
    return prepared_data


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
    """
    :param payload: item list
    :return: name of created file
    """
    if 'components' in payload[0]:
        nested_components = get_nested_components(payload)
        items = get_items(payload)
        merge_data = {**items, **nested_components}
        index = get_indices(merge_data)
        filename = os.getcwd() + \
                   '/media/generated/Отчёт_' + \
                   dt.datetime.now().strftime('%d-%m-%Y_%H:%M:%S') + '.xlsx'
        # dt.datetime.now().strftime('%d-%m-%Y_%H:%M:%S')
        temp_df = pd.DataFrame(data=merge_data, index=index)
        temp_df.to_excel(filename, sheet_name='Main')

    else:
        filename = write(payload)

    result_path = make_archive(os.getcwd() + '/media/Документы_' + dt.datetime.now().strftime('%d-%m-%Y'),
                               'zip',
                               root_dir=os.getcwd() + '/media/generated',
                               base_dir='.')
    return result_path
