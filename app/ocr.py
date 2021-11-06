# -*- coding:utf-8 -*-

import cv2
import datetime
import hashlib
import logging
import numpy as np
import pytesseract
import string

from flask import Blueprint
from flask import jsonify
from flask import request
from app import db
from .models import OcrResultData

ocr = Blueprint('ocr', __name__)

logger = logging.getLogger(__name__)

@ocr.route('/index')
def index():
    return "Hello world"


@ocr.route('/get_ocr_result/', methods=['POST'])
def get_ocr_result():
    if request.method == 'POST':
        upload_img = request.files['file']
        file_name = upload_img.filename
        file_type = file_name.split('.')[-1]
        file_data = upload_img.read()
        content = []
        if file_data:
            file_hash_code = get_md5_hash(file_data)
            # search the same code in the database and find the result if needed
            new_file_path = './media_dir' + '/' + file_hash_code + '.' + file_type
            with open(new_file_path, 'wb') as f:
                f.write(file_data)
            upload_time = datetime.datetime.now()
            string_result = get_alphabet_string(new_file_path)
            ocr_obj = OcrResultData(file_name=file_name, file_hash_code=file_hash_code, upload_time=upload_time,
                                    content=string_result)
            db.session.add(ocr_obj)
            db.session.commit()
            content = list(string_result)
        result = dict(content=content)
        return jsonify(result)


def get_alphabet_string(file_path):
    # get alphabet string
    img = cv2.imread(file_path)
    gray_img = get_grayscale(img)
    morphology_img = opening(gray_img)
    raw_string_result = pytesseract.image_to_string(morphology_img, lang='eng')
    string_result_list = [raw_char for raw_char in raw_string_result if raw_char in string.ascii_letters]
    string_result = ''.join(string_result_list)
    return string_result


def get_md5_hash(file_data):
    # get image md5 code
    md5obj = hashlib.md5()
    md5obj.update(file_data)
    hash_code = md5obj.hexdigest()
    return hash_code


def get_grayscale(img):
    # get grayscale image
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def opening(img):
    # opening - erosion followed by dilation
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
