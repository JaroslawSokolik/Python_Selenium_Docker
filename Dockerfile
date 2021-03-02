FROM python:3.7
RUN mkdir ./tests
COPY . /tests
WORKDIR /tests
RUN pip install -r requirements.txt
ENV DISPLAY=:99