# -*- coding:utf-8 -*-

from app import db 


class OcrResultData(db.Model):
    """save ocr result data"""
    __tablename__ = 'orc_data'
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255))
    file_hash_code = db.Column(db.String(64))
    upload_time = db.Column(db.DateTime())
    content = db.Column(db.Text())
