FROM python3.7-alpine

COPY Pipfile Pipfile.lock /

RUN pipenv sync

COPY . /app

WORKDIR /app

CMD ["/bin/sh", "start.sh"]
