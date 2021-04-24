from PIL import Image
import pytesseract
import cv2
import os
import numpy as np

def to_gray(image: str):
    preprocess = "blur"

    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)

    filename = 'tmp.png'
    cv2.imwrite(filename, gray)
    return filename


def recognizer(image):
    img = cv2.imread(image)
    name_img = img[0:500, 400:1200]
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    name_img = cv2.filter2D(name_img, -1, kernel)
    cv2.imwrite("name.png", name_img)
    text = pytesseract.image_to_string(Image.open("name.png"), lang='rus+eng')
    if text.find('наименование') != -1:
        return text[text.find('наименование') + len('наименование'):] \
            .replace("\n", " ") \
            .strip()

    else:
        name_img = img[660:1800, :620]
        cv2.imwrite("name.png", name_img)
        return pytesseract.image_to_string(Image.open("name.png"), lang='rus+eng') \
            .replace("\n", " ") \
            .strip()

