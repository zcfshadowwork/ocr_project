# -*- coding:utf-8 -*-

from app import app
from .ocr import ocr

app.register_blueprint(ocr, url_prefix='/ocr')
