FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt

RUN mkdir /app/
COPY ./app /app/
WORKDIR /app/