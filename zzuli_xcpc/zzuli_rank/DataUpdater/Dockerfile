FROM python:3.9-alpine

RUN mkdir -p /home/python/data_updater

WORKDIR /home/python/data_updater

COPY requirements.txt .

RUN pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main_updater.py"]