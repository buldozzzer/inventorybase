import cv2
import numpy as np
import pytesseract
from PIL import Image
import os


def sort_by(val):
    return val[0]


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def recognizer(filename):
    # Поворот изображения в горизонтальное положение
    os.system('tesseract --psm 0 {} text'.format(filename))
    im = Image.open(filename)
    file = open('text.osd', 'r')
    for line in file:
        if line.find('Orientation in degrees:') != -1:
            line = line[len('Orientation in degrees:'):]
            im.transpose(int(int(line.replace('\n', '').strip()) / 90 + 1)).save(filename)
    os.remove('text.osd')
    image = cv2.imread(filename)
    # Предобработка изображения перед распознаванием
    gray_image = image[:, :, 0]
    ret, thresh_value = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((2, 2), np.uint8)
    dilated_value = cv2.dilate(thresh_value, kernel, iterations=1)
    # Вычисление координат контуров ячеек
    contours, hierarchy = cv2.findContours(dilated_value, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    coordinates = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if h > 50 and w > 50 and h * w < 350000:
            coordinates.append((x, y, w, h))

    # Сортровка по столбцам таблицы и формирование массивов столбцов
    recognized_table = row = []
    prev_y = 0
    coordinates.sort()
    coordinates.sort(key=sort_by)
    for coord in coordinates:
        x, y, w, h = coord
        if y > prev_y + 5:
            recognized_table.append(row)
            row = []
        crop_img = image[y:y + h, x:x + w]
        recognized_string = pytesseract.image_to_string(crop_img, lang="rus+eng")
        row.append(recognized_string.replace("\n", " ").strip())
        prev_y = y

    result_extracting_data = {}

    for column in recognized_table:
        if 'наименование' in column:
            result_extracting_data['name'] = column
            result_extracting_data['name'].remove('наименование')
        elif 'Наименование' in column:
            result_extracting_data['name'] = column
            result_extracting_data['name'].remove('Наименование')
        if 'количество' in column:
            counts = []
            for cell in column:
                cell = cell.replace(',', '.')
                if is_number(cell):
                    counts += [int(float(cell))]
            result_extracting_data['count'] = counts
        elif 'Количество' in column:
            counts = []
            for cell in column:
                cell = cell.replace(',', '.')
                if is_number(cell):
                    counts += [int(float(cell))]
                print(counts)

            result_extracting_data['count'] = counts

    result_extracting_data['items'] = []
    index = 1
    for name, count in zip(result_extracting_data['name'],
                           result_extracting_data['count']):
        result_extracting_data['items'].insert(0, {'name': name,
                                                   'count': count,
                                                   'index': index,
                                                   'inventory_n': ''})
        index += 1
    result_extracting_data.pop('name')
    result_extracting_data.pop('count')

    os.remove(filename)
    return result_extracting_data
