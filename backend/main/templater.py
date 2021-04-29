from pathlib import Path
from shutil import make_archive
import os
import re
from slugify import slugify
from docx.shared import Pt
import docx
import pandas as pd

ALLOWED_EXTENSIONS = {'docx', 'xlsx'}
ALLOWED_TEMPLATES = {
    'name': '{{наименование}}',
    'inventory_n': '{{инвентарный номер}}',
    'responsible': '{{ответственный сотрудник}}',
    'otss_category': '{{отсс}}',
    'condition': '{{состояние}}',
    'unit_from': '{{откуда поступила}}',
    'in_operation': '{{используется}}',
    'fault_document_requisites': '{{документы о неисправности}}',
    'date_of_receipt': '{{дата поступления}}',
    'number_of_receipt': '{{номер требования}}',
    'requisites': '{{реквизиты книги учета}}',
    'transfer_date': '{{дата передачи}}',
    'otss_requisites': '{{реквизиты отсс}}',
    'spsi_requisites': '{{реквизиты спси}}',
    'transfer_requisites': '{{реквизиты о передаче}}',
    'last_check': '{{последняя проверка}}',
    'comment': '{{примечания}}',
    'user': '{{кому передали}}',
    'components': '{{компоненты}}'
}


def find_docx_templates(doc):
    """
    Поиск всех шаблонов в docx документе
    :param doc(Document(file)) - открытый docx-файл
    :return: set(шаблонов)
    """
    templates = []
    try:
        for paragraph in doc.paragraphs:
            for match in re.finditer('\\{\\{.*?\\}\\}', paragraph.text):
                templates.insert(0, match.group(0))
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    templates = templates.union(find_docx_templates(cell))
    except AttributeError as error:
        print(error)
        # log.exception('Error with {}'.format(str(error)))

    sorted(list(templates))
    return templates


def get_docx_templates(filename):
    """
    Метод для получения шаблонов из docx файла
    :return: set(шаблонов)
    """
    docx_templates = []
    try:
        doc = docx.Document(filename)
        docx_templates = find_docx_templates(doc)
    except AttributeError as error:
        print(error)
        # log.exception('Error with {}'.format(str(error)))

    return docx_templates


def check_templates(all_templates):
    global ALLOWED_TEMPLATES
    correct_templates = ALLOWED_TEMPLATES.values()
    incorrect_templates = set()
    for template in all_templates:
        if template not in correct_templates:
            incorrect_templates.add(template)
    return incorrect_templates


def prep_data(payload: list):
    global ALLOWED_TEMPLATES
    keys = ALLOWED_TEMPLATES.keys()
    prep_payload = []
    for item in payload:
        prep_item = {}
        for field in item:
            prep_item[ALLOWED_TEMPLATES[field]] = item[field]
        prep_payload.insert(0, prep_item)
    return prep_payload
