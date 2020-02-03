FROM python:3.7.6

MAINTAINER hckcksrl <hckcksrl@naver.com>

RUN mkdir cafe
COPY Pipfile ./cafe
COPY Pipfile.lock ./cafe
COPY . ./cafe
WORKDIR /cafe
RUN pip3 install pipenv
RUN pipenv install --system


EXPOSE 8000


CMD ["python","manage.py","runserver","0.0.0.0:8000"]