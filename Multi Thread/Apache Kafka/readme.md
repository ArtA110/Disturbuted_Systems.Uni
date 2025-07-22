# How to run
## create virtual environment
```bash
python3 -m virtualenv .venv
```
**If you are in windows use ```python``` insetead of ```python3```**

## Install requirements
```bash
pip install -r requirements.txt
```
## Run Project
```
docker compose up -d
python producer.py && python consumer.py
```

**```Ctrl+C``` for end the program**