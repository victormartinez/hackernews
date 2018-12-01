FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN mkdir /code

WORKDIR /code

ADD . /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -e 'git+https://github.com/jschneier/django-storages.git#egg=django-storages'

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "config.wsgi", "--log-file", "-"]
