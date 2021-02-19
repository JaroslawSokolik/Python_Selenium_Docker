FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN pip install pytest
RUN pip install selenium

RUN mkdir /app/
COPY ./app /app/
WORKDIR /app/
CMD ["python3", "bot.py"]