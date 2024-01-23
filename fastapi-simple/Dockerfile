# 
FROM python:3.10

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["gunicorn","-k", "uvicorn.workers.UvicornWorker", "-w", "4","-t", "64" ,"-b", "0.0.0.0:80", "app.app:app"]