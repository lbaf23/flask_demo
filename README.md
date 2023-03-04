# Flask Demo

- [Flask](https://flask.net.cn/) Restful API
  - with crud examples
- MySQL [Flask-SQLAlchemy — Flask-SQLAlchemy Documentation (3.0.x) (palletsprojects.com)](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)

## dev
- install
```bash
pip install -r requirements.txt
```

- set config
```bash
cp config.py config_dev.py
```
> set mysql user and password in config_dev.py
> 
> create database `demo`

- run
```bash
python app.py
```

- generate requirements.txt
```bash
pip install pipreqs
pipreqs ./ --force --encoding='utf-8'
```
