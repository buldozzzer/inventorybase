from PIL import Image
import pytesseract
import cv2
import os


def recognizer(image):
    preprocess = "blur"

    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # удаление шумов
    if preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)

    elif preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    filename = "{}.jpg".format(os.getpid())
    cv2.imwrite(filename, gray)

    text = pytesseract.image_to_string(Image.open(filename), lang='rus+eng')
    os.remove(filename)
    return text
