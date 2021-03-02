FROM python:3.7
ADD . /tests
WORKDIR /tests
RUN pip install -r requirements.txt
ENV DISPLAY=:99