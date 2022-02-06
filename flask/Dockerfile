FROM  python:3.7.2-stretch
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
ENTRYPOINT ["uwsgi", "app.ini"]