FROM python:3.8

LABEL maintainer="Dave Heuts dheuts@deofficespecialist.nl"

WORKDIR /user/src/app

COPY './requirements.txt' .

RUN pip install -r requirements.txt

COPY ./app .

ENTRYPOINT ['python3', 'app.py']