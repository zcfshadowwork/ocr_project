# -*- coding:utf-8 -*-

import logging

def get_logger(name):
    # create logger
    logger = logging.getLogger(name)
    # create file handler
    handler = logging.FileHandler('flask_{}.log'.format(name), encoding='UTF-8')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.addHandler(console_handler)
    return logger