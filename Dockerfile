FROM python:3.8

RUN apt-get update
RUN apt-get install python3-pip -y

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]