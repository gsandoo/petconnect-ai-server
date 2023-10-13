FROM python:3.7

RUN apt-get -y update
COPY requirements.txt myapp/requirements.txt

RUN pip install -r requirements.txt
RUN pip install opencv_python-3.4.2.16-cp37-cp37m-win_amd64.whl
RUN pip install opencv_contrib_python-3.4.2.16-cp37-cp37m-win_amd64.whl
EXPOSE 5000
CMD ["python", "app.py" ]
