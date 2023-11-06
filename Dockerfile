FROM python:3.10-alpine
ENV PYTHONBUFFERED 1
WORKDIR /django_web

COPY requirements.txt /django_web	

RUN pip install -r requirements.txt

COPY . /django_web

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
