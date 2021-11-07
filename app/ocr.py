# -*- coding:utf-8 -*-

import datetime

from flask import abort
from flask import Blueprint
from flask import jsonify
from flask import request
from app import db
from .models import OcrResultData
from .tools import get_alphabet_string
from .tools import get_md5_hash
from .logger import get_logger

ocr = Blueprint('ocr', __name__)

logger = get_logger(__name__)


@ocr.route('/index')
def index():
    """
    test
    """
    return "Hello world"


@ocr.route('/get_ocr_result/', methods=['POST'])
def get_ocr_result():
    """
    get image ocr result
    """
    if request.method == 'POST':
        upload_img = request.files['file']
        file_name = upload_img.filename
        file_format = file_name.split('.')[-1]
        logger.info("{} ocr start!".format(file_name))
        # check if image format is jpg or png
        if file_format.lower() not in ('jpg', 'png'):
            logger.error("file_name: {} wrong image format".format(file_name))
            abort(404, description="Please check the file format")
        file_data = upload_img.read()
        content = []
        if file_data:
            file_hash_code = get_md5_hash(file_data)
            # search the same code in the database and find the result if needed
            save_file_path = './media_dir' + '/' + file_hash_code + '.' + file_format
            # save imgage file to media_dir
            with open(save_file_path, 'wb') as f:
                f.write(file_data)
            upload_time = datetime.datetime.now()
            try:
                string_result = get_alphabet_string(save_file_path)
            except Exception as e:
                logger.error("recoginize image eror, {}".format(e))
                abort(404, description="Recoginize image error")
            # save ocr result
            ocr_obj = OcrResultData(file_name=file_name, file_hash_code=file_hash_code, upload_time=upload_time,
                                    content=string_result)
            db.session.add(ocr_obj)
            db.session.commit()
            content = list(string_result)
        logger.info("{} ocr end!".format(file_name))
        result = dict(content=content)
        return jsonify(result)

