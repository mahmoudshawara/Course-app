FROM  python:3.9-slim
COPY . /app
WORKDIR /app
ENV POSTGRES_USER: postgres \
    POSTGRES_PASSWORD: 1234 \
    POSTGRES_HOST: localhost \    
    POSTGRES_PORT: 5432 \
    POSTGRES_DB: school 
RUN pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

EXPOSE 5000
ENTRYPOINT ["python","app.py"]

