ARG APP_NAME=app
ARG APP_PATH=/opt/$APP_NAME

FROM python:3.9
ARG APP_NAME
ARG APP_PATH

WORKDIR $APP_PATH

COPY ./requirements.txt $APP_PATH/requirements.txt

RUN pip install --no-cache-dir --upgrade -r $APP_PATH/requirements.txt

COPY ./app $APP_PATH/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]