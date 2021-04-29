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
    prep_payload = []
    for item in payload:
        prep_item = {}
        for field in item:
            prep_item[ALLOWED_TEMPLATES[field]] = item[field]
            if prep_item[ALLOWED_TEMPLATES[field]] is None:
                prep_item[ALLOWED_TEMPLATES[field]] = ''
        prep_payload.insert(0, prep_item)
    return prep_payload


def docx_write(document, substr, replace):
    """
    Основная функция для замены шаблонов из таблицы
    в docx-документ
    :param document: Document(file) - открытый docx-файл
    :param substr: Первая строка в одном из наборов mini_dict
    :param replace: Вторая строка в одном из наборов mini_dict
    :return:
    """
    # style = document.styles['Normal']
    # font = style.font
    # font.name = 'Times New Roman'
    # font.size = Pt(14)

    for parg in document.paragraphs:
        if substr in parg.text:
            inline = parg.runs
            was_replaced = False
            for i in range(len(inline)):
                if substr in inline[i].text:
                    text = inline[i].text.replace(substr, replace)
                    was_replaced = True
                    inline[i].text = text
            if not was_replaced:
                text = parg.text.replace(substr, replace)
                parg.text = text
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                docx_write(cell, substr, replace)


def final_replacement(filename: str, payload: list):
    final_data = prep_data(payload)
    replaceable_templates = get_docx_templates(filename)
    for item, i in zip(final_data, range(len(final_data))):
        document = docx.Document(filename)
        for template in replaceable_templates:
            try:
                docx_write(document, template, str(item[template]))
                if os.name == 'nt':
                    document.save('Документ-{}.docx'.format(i + 1))
                elif os.name == 'posix':
                    document.save('Документ-{}.docx'.format(i + 1))
            except KeyError as error:
                continue
