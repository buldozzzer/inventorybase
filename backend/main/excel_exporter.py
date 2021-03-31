import pandas as pd
import datetime as dt


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
        ('Компоненты', 'Вид'): {}, ('Компоненты', 'Категория'): {},
        ('Компоненты', 'Год выпуска'): {}, ('Компоненты', 'Цена'): {},
        ('Компоненты', 'Местонахождение'): {}
    }

    component_titles = ['name', 'serial_n', 'type', 'view', 'category', 'year', 'cost', 'location']

    for key, title in zip(component_titles, nested_components):
        component_cell = {}
        for i in range(len(payload)):
            for j in range(len(payload[i]['components'])):
                component_cell[(i + 1, j + 1)] = payload[i]['components'][j][key]
        nested_components[title] = component_cell

    for sample in nested_components[('Компоненты', 'Местонахождение')]:
        nested_components[('Компоненты', 'Местонахождение')][sample] = \
            'Объект: ' + nested_components[('Компоненты', 'Местонахождение')][sample]['object'] + \
            ',\nкорпус: ' + nested_components[('Компоненты', 'Местонахождение')][sample]['object'] + \
            ',\nкабинет: ' + nested_components[('Компоненты', 'Местонахождение')][sample]['object'] + \
            ',\nподразделние: ' + nested_components[('Компоненты', 'Местонахождение')][sample]['object']

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

    tuples = list(zip(*arrays))
    tuples.sort(key=lambda key: key[0])

    index = pd.MultiIndex.from_tuples(tuples, names=[None, None])

    return index


def export_to_excel(payload: list):
    """
    :param payload: item list
    :return: name of created file
    """
    nested_components = {}

    if 'components' in payload[0]:
        nested_components = get_nested_components(payload)

    items = get_items(payload)

    merge_data = {**items, **nested_components}

    index = get_indices(merge_data)

    filename = 'report_' + dt.datetime.now().strftime('%d-%m-%Y_%H:%M:%S') + '.xlsx'

    temp_df = pd.DataFrame(data=merge_data, index=index)
    temp_df.to_excel(filename, sheet_name='Main')

    return filename
