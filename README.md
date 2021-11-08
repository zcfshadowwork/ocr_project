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

## How to test or use

You can use the testing script `test.py` in `test` directory


```
$ python test.py
    result:
```
![avatar](test//1.png)
```
    1.png {"content":["o","c","r"]}
```
![avatar](test//2.png)
```
    2.png {"content":["S","e","a","r","c","h","P","r","e","v","i","e","w"]}
```

 ![avatar](test//3.jpg)
 ```
    3.jpg {"content":["L","e","t","t","e","r","W","r","i","t","i","n","g"]}
 ```
 ![avatar](test//4.png)
 ```
    4.png {"content":["z","M","e","d","i","c","i","n","e"]}
 ```
 
  ![avatar](test//5.png)
  ```
    5.png {"content":["T","h","r","o","u","g","h","o","u","t","t","h","e","c","o","u","r","s","e","o","f","t","h","e","r","i","v","e","r","t","h","e","t","o","t","a","l","v","o","l","u","m","e","o","f","w","a","t","e","r","t","r","a","n","s","p","o","r","t","e","d","d","o","w","n","s","t","r","e","a","m","w","i","l","l","o","f","t","e","n","b","e","a","c","o","m","b","i","n","a","t","i","o","n","o","f","t","h","e","f","r","e","e","w","a","t","e","r","f","l","o","w","t","o","g","e","t","h","e","r","w","i","t","h","a","s","u","b","s","t","a","n","t","i","a","l","v","o","l","u","m","e","f","l","o","w","i","n","g","t","h","r","o","u","g","h","s","u","b","s","u","r","f","a","c","e","r","o","c","k","s","a","n","d","g","r","a","v","e","l","s","t","h","a","t","u","n","d","e","r","i","l","e","t","h","e","r","i","v","e","r","a","n","d","I","t","s","f","l","o","o","d","p","l","a","i","n","c","a","l","l","e","d","t","h","e","h","y","p","o","r","h","e","k","c","z","o","n","e","F","o","r","m","a","n","y","r","i","v","e","r","s","I","n","l","a","r","g","e","v","a","l","l","e","y","s","t","h","i","s","u","n","s","e","e","n","c","o","m","p","o","n","e","n","t","o","f","f","l","o","w","m","a","y","g","r","e","a","t","l","y","e","x","c","e","e","d","t","h","e","v","i","s","i","b","l","e","f","l","o","w"]}
  ```
 ![avatar](test//6.jpg)
 ```
    6.jpg {"content":[]}
 ```
 
 ![avatar](test//7.jpg)
 ```
    7.jpg {"content":["B","R","E","A","K","I","N","G","T","H","E","S","T","A","T","U","E","i","h","a","v","e","a","l","w","a","y","s","k","n","o","w","n","i","j","u","s","t","d","i","d","n","t","u","n","d","e","r","s","t","a","n","d","t","h","e","i","n","n","e","r","c","o","n","f","l","i","c","t","i","o","n","s","a","r","r","e","s","t","i","n","g","o","u","r","h","a","n","d","s","g","r","a","v","i","t","a","t","i","n","g","c","l","o","s","e","e","n","o","u","g","h","e","x","p","a","n","s","i","v","e","d","i","s","t","a","m","c","e","b","e","t","w","e","e","n","c","o","u","l","d","n","t","g","i","v","e","y","o","u","m","o","r","e","b","u","t","m","e","a","n","t","e","v","e","r","y","t","h","i","n","g","w","h","e","n","t","h","e","d","a","y","c","o","m","e","s","y","o","u","f","i","n","d","y","o","u","r","h","e","a","r","t","w","a","n","t","s","s","o","m","e","t","h","i","n","g","m","o","r","e","t","h","a","n","a","v","i","e","c","e","a","n","d","a","p","a","r","t","y","o","u","r","l","i","f","e","w","i","l","l","c","h","a","n","g","e","l","i","k","e","a","s","t","a","t","u","e","s","e","t","f","r","e","e","t","o","w","a","l","k","a","m","o","n","g","u","s","t","o","c","r","e","a","t","e","d","e","s","t","i","n","y","w","e","d","i","d","n","t","b","r","e","a","k","a","n","y","r","u","l","e","s","w","e","d","i","d","n","t","m","a","k","e","m","i","s","t","a","k","e","s","m","a","k","i","n","g","b","e","a","u","t","y","i","n","l","o","v","i","n","g","m","a","k","i","n","g","l","o","v","i","n","e","f","o","r","d","a","y","s","S","H","I","L","O","W"]}
```
 ![avatar](test//8.png)
```
    8.png ["r","h","y","x","C","h","i","n","e","s","e","A","E","D","E","E","S","O","E","O","I","S","A","U","C","E","S","i","p","u","m","e","e","e","A","t","t","t","o","r","t","e"]}
```
then the images in this directory will send to the flask_app service and return the ocr result

You can also use curl or Postman to test this service, post a 'jpg' or 'png' image to url 'http://127.0.0.1:9014/ocr/get_ocr_result/'

```
$ curl http://127.0.0.1:9014/ocr/get_ocr_result/ -F "file=@file_path"
```

## Future

we can see, The orc result is not 100% accurate, when mixed with Chinese characters, it will recognize all as alphabets and makes mistakes.

it demands a lot of improvement in the future.
 