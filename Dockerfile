FROM python:3.7
COPY . /app
COPY requirements.txt myapp/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "app.py"]