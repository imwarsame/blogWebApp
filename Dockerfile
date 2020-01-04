FROM python:3

MAINTAINER daniel@federschmidt.xyz

COPY . /app
WORKDIR /app


RUN pip install pipenv
RUN pipenv install --deploy

EXPOSE 5000

CMD ["python", "run.py"]
