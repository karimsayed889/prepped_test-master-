# Dockerizing backend App 
FROM python:3.10

RUN mkdir /app

ADD . /app

RUN pip install -r /app/requirements.txt

CMD ["python","/app/app.py"]
