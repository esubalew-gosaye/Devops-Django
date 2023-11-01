FROM python:3.10

WORKDIR django_web

COPY requirements.txt django_web	

RUN pip install requirements.txt

COPY . django_web

EXPOSE 8080

CMD ["python", "manage.py", "runserver"]