FROM python:3.10
ENV PYTHONBUFFERED 1
WORKDIR /django_web

COPY requirements.txt /django_web	

RUN pip3 install -r requirements.txt

COPY . /django_web

EXPOSE 8001

CMD ["python3", "manage.py", "runserver"]