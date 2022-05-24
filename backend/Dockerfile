FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN apk update \
  && apk add gcc libc-dev g++ \
  && apk add libffi-dev libxml2 libffi-dev \
  && apk add unixodbc-dev mariadb-dev python3-dev
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /code/

CMD ["python", "main.py"]
