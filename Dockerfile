FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
ADD . /tests
WORKDIR /tests
RUN pip install -r requirements.txt
CMD python bot.py