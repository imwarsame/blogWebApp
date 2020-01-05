FROM python:3.7

MAINTAINER imwarsame

WORKDIR /usr/src/flaskblog
COPY . .


RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000

CMD ["python", "./run.py"]
