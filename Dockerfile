FROM python

COPY . /app
WORKDIR /app

RUN echo server will be running on 5000
RUN pip install flask
RUN pip install flask-migrate
RUN pip install flask-sqlalchemy



CMD ["python" , "test.py"]

