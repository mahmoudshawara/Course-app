FROM  python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
EXPOSE 5000
ENTRYPOINT ["python","app.py"]

