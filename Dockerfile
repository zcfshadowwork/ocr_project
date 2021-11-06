FROM python:latest

RUN apt-get update && \
    apt-get -y install \
    tesseract-ocr \
    libgl1-mesa-dev && \
    apt-get clean

EXPOSE 5000
WORKDIR /code
COPY app app/
COPY media_dir media_dir/
COPY *.py /code/
COPY requirements.txt /code/
RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple && \
    pip install \
    pillow  \
    opencv-python \
    pytesseract -i https://mirrors.aliyun.com/pypi/simple  && \
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
ENTRYPOINT ["/usr/bin/tail", "-f", "/dev/null"]
# ENTRYPOINT ["python3", "run.py"]
# CMD ["gunicorn", "run:app", "-c", "./gunicorn.conf.py"]