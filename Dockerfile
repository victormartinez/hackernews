FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN mkdir /code

WORKDIR /code

ADD . /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "config.wsgi", "--log-file", "-"]
