# Flask Demo

- Flask restful api
  - with crud example
- MySQL

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
