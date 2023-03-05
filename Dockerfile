FROM python:3.8
WORKDIR /flask_demo

COPY requirements.txt .

RUN pip install gunicorn gevent pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .
CMD ["gunicorn", "app:app", "-c", "gunicorn.conf.py"]
