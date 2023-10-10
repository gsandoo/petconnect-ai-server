FROM python:3.7

RUN apt-get update
RUN apt-get install python3-pip -y

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "app.py"]