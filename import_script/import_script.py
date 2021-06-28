import fire
import pandas as pd
import pymongo

items = []


def prep_data(filename):
    data_frame = pd.read_excel(filename, sheet_name=0)

    for i in range(data_frame.shape[0]):
        item_entity = {
            'name': '',
            'user': '',
            'responsible': '',
            'components': [],
            'inventory_n': '',
            'otss_category': '',
            'condition': '',
            'unit_from': '',
            'in_operation': '',
            'fault_document_requisites': '',
            'date_of_receipt': '',
            'number_of_receipt': '',
            'requisites': '',
            'transfer_date': '',
            'otss_requisites': '',
            'spsi_requisites': '',
            'transfer_requisites': '',
            'comment': '',
            'last_check': '',
            'serial_n': '',
            'category': '',
            'year': '',
            'cost': '',
            'location_object': '',
            'location_corpus': '',
            'location_cabinet': ''
        }
        items.append(item_entity)

    for item, value in zip(items, data_frame['Наименование']):
        if type(value) == float:
            value = ''
        item['name'] = value

    for item, value in zip(items, data_frame['Сотрудник МатОтвЛицо']):
        if type(value) == float:
            value = ''
        item['responsible'] = value

    for item, value in zip(items, data_frame['Инвентарный номер']):
        if type(value) == float:
            value = ''
        item['inventory_n'] = value

    for item, value in zip(items, data_frame['Сотрудник, которому передано в пользование']):
        if type(value) == float:
            value = ''
        item['user'] = value

    for item, value in zip(items, data_frame['Примечание']):
        if type(value) == float:
            value = ''
        item['comment'] = value

    for item, value in zip(items, data_frame['СостояниеТехники']):
        if type(value) == float:
            value = ''
        item['condition'] = value

    for item, value in zip(items, data_frame['Категория ОТСС  ']):
        if type(value) == float:
            value = ''
        item['otss_category'] = value

    for item, value in zip(items, data_frame['Дата поступления на учет  ']):
        if type(value) == float:
            value = ''
            item['date_of_receipt'] = value
        else:
            splited_date = str(value).split('.')
            formated_value = splited_date[2] + '-' + splited_date[1] + '-' + splited_date[0]
            item['date_of_receipt'] = formated_value

    for item, value in zip(items, data_frame['Реквезит документа о прохождСПСИ']):
        if type(value) == float:
            value = ''
        item['spsi_requisites'] = value

    for item, value in zip(items, data_frame['Реквезит документа о поступлении  ']):
        if type(value) == float:
            value = ''
        item['requisites'] = value

    for item, value in zip(items, data_frame['Реквезит о передаче во временное пользование  ']):
        if type(value) == float:
            value = ''
        item['transfer_requisites'] = value

    for item, value in zip(items, data_frame['Реквезит документа о передаче МатОтвЛицу']):
        if type(value) == float:
            value = ''
        item['fault_document_requisites'] = value

    for item, value in zip(items, data_frame['Реквезит документа о категории  ']):
        if type(value) == float:
            value = ''
        item['otss_requisites'] = value

    for item, value in zip(items, data_frame['Подразделение откуда поступило']):
        if type(value) == float:
            value = ''
        item['unit_from'] = value

    for item, value in zip(items, data_frame['Дата передачи Мц']):
        if type(value) == float:
            value = ''
            item['transfer_date'] = value
        else:
            splited_date = str(value).split('.')
            formated_value = splited_date[2] + '-' + splited_date[1] + '-' + splited_date[0]
            item['transfer_date'] = formated_value


def set_conn(host: str, port: int):
    __db_conn = pymongo.MongoClient(host=host, port=port)
    return __db_conn


def get_conn(host: str = 'items_db', db_name: str = 'ItemsDB'):
    __db_conn = None
    if not __db_conn:
        __db_conn = set_conn(
            host=host,
            port=27017)
    return __db_conn[db_name]


class Importer:

    def insert_data(self, filename: str, host: str = 'items_db'):
        prep_data(filename)
        collection = get_conn(host)['main_item']
        if collection:
            result = collection.insert_many(items)
            return result.inserted_ids
        else:
            return "connection is refused"


if __name__ == '__main__':
    fire.Fire(Importer)
