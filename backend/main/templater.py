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
    '{{наименование}}',
    '{{инвентарный номер}}',
    '{{ответственный сотрудник}}',
    '{{отсс}}',
    '{{состояние}}',
    '{{откуда поступила}}',
    '{{используется}}',
    '{{документы о неисправности}}',
    '{{дата поступления}}',
    '{{номер требования}}',
    '{{реквизиты книги учета}}',
    '{{дата передачи}}',
    '{{реквизиты отсс}}',
    '{{реквизиты спси}}',
    '{{реквизиты о передаче}}',
    '{{последняя проверка}}',
    '{{примечания}}',
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
