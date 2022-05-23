FROM python:3.9

COPY ./app ./app
COPY ./requirements.txt ./requirements.txt
COPY ./config.py ./config.py

RUN pip install --no-cache-dir -r ./requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]