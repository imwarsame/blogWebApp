FROM python:3

MAINTAINER imwarsame

COPY . /app
WORKDIR /app


RUN pip install pipenv
RUN pipenv install --deploy

EXPOSE 5000

CMD ["python", "run.py"]
