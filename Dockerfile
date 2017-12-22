FROM python:3.6-alpine

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 server:app --reload --log-level debug
