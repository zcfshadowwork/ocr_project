# -*- coding:utf-8 -*-

import cv2
import hashlib
import numpy as np
import pytesseract
import string


def get_alphabet_string(file_path):
    """
    get alphabet string
    """
    img = cv2.imread(file_path)
    gray_img = get_grayscale(img)
    morphology_img = opening(gray_img)
    raw_string_result = pytesseract.image_to_string(morphology_img, lang='eng')
    string_result_list = [raw_char for raw_char in raw_string_result if raw_char in string.ascii_letters]
    string_result = ''.join(string_result_list)
    return string_result


def get_md5_hash(file_data):
    """
    get image md5 code
    """
    md5obj = hashlib.md5()
    md5obj.update(file_data)
    hash_code = md5obj.hexdigest()
    return hash_code


def get_grayscale(img):
    """
    get grayscale image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def opening(img):
    """
    opening - erosion followed by dilation
    """
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
