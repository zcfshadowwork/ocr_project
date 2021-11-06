# -*- coding:utf-8 -*-

import requests



def test_1():
    url = 'http://127.0.0.1:5000/ocr/get_ocr_result/'

    files = {'file': open('1.jpg', 'rb')}

    res = requests.post(url, files=files)

    import pdb;pdb.set_trace()

def test_2():
    url = 'http://127.0.0.1:5000/ocr/'

    res = requests.get(url)

    import pdb;pdb.set_trace()


if __name__ == '__main__':
    test_1()