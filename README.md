# ocr_project
`ocr_project` contains a light Flask web service using for Etruscan alphabet recognition with features:
- Use Flask as the web framwork
- Use Tesseract to recognize alphabets in .jpg or .png images 
- Use MySQL for result data saving
- Use gunicorn and gevent to support multiprocessing and coroutine call
- Run in Docker 

## How to start

Linux is preferred to run this project, please make sure you have installed Docker and docker-compose when run the commands below

```
$ mkdir Project
$ cd Project
$ git clone https://github.com/zcfshadowwork/ocr_project.git .
$ cd ocr_project
$ docker-compose up -d
```
After containers have been built, enter the flask_mysql container to create the ocr_database
```
$ docker exec -it flask_mysql /bin/bash
$ mysql -uroot -p
$ root
$ create database ocr_database;
```
Then enter the flask_app container, run the script to create the ocr_datatable;
```
$ docker exec -it flask_app /bin/bash
$ python3 create_db.py
```

## Project structure


    ├── app
    │   ├── __init__.py
    │   ├── logger.py
    │   ├── models.py
    │   ├── ocr.py
    │   ├── tools.py
    │   └── views.py
    ├── config.py
    ├── create_db.py
    ├── docker-compose.yml
    ├── Dockerfile
    ├── gunicorn.conf.py
    ├── media_dir
    ├── README.md
    ├── requirements.txt
    ├── run.py
    └── test
        ├── 1.jpg
        ├── 2.png
        ├── 3.png
        ├── ...
        └── test.py
        
`docker-compose.yml` and ``Dockerfile`` files to build Flask and MySQL containers

`create_db.py`  the script to create table in ocr_database

`config.py`  specifys the config  for this flask service

`gunicorn.conf.py` specifys the gunicorn config, you can set the worker number, binding host and port 

`run.py`  the script to run the Flask service

`requirements.txt`  specifys what python packages are required to run the project

`logger.py`  define logger settings and formatters

`models.py` defines the database model

`ocr.py` main service file 

`tools.py` contains some functions to deal with image file

`views.py` register orc as buleprint

## How to test

You can use the testing script `test.py` in `test` directory

```
$ python test.py
```
then the images in this directory will send to the flask_app service and return the ocr result

You can also use Postman to test this service, post a 'jpg' or 'png' image to url 'http://127.0.0.1:5000/ocr/get_ocr_result/'
