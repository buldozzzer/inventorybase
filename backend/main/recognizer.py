import cv2
import numpy as np
import pytesseract
from PIL import Image
import os


# def to_gray(image: str):
#     preprocess = "blur"
#
#     image = cv2.imread(image)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#     if preprocess == "thresh":
#         gray = cv2.threshold(gray, 0, 255,
#                              cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#
#     elif preprocess == "blur":
#         gray = cv2.medianBlur(gray, 3)
#
#     filename = 'media/tmp.png'
#     cv2.imwrite(filename, gray)
#     return filename
#
#
# def recognizer(image):
#     filename = to_gray(image)
#     img = cv2.imread(filename)
#     name_img = img[80:450, 450:1150]
#     kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
#     name_img = cv2.filter2D(name_img, -1, kernel)
#     cv2.imwrite("media/name.png", name_img)
#     text = pytesseract.image_to_string(Image.open("media/name.png"), lang='rus+eng')
#     if text.find('наименование') != -1:
#         os.remove('media/tmp.png')
#         os.remove('media/name.png')
#         os.remove(image)
#         return text[text.find('наименование') + len('наименование'):] \
#             .replace("\n", " ") \
#             .strip()
#     else:
#         name_img = img[660:1800, :620]
#         cv2.imwrite("media/name.png", name_img)
#         text = pytesseract.image_to_string(Image.open("media/name.png"), lang='rus+eng') \
#             .replace("\n", " ") \
#             .strip()
#         os.remove('media/tmp.png')
#         os.remove('media/name.png')
#         os.remove(image)
#         return text[text.find('наименование') + len('наименование'):] \
#             .replace("\n", " ") \
#             .strip()

def sort_by(val):
    return val[0]


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
        elif 'Наименование' in column:
            result_extracting_data['name'] = column
        if 'количество' in column:
            result_extracting_data['count'] = column
        elif 'Количество' in column:
            result_extracting_data['count'] = column

    os.remove(filename)
    return result_extracting_data
