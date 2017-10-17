FROM python:2.7

ADD . /code
WORKDIR /code
ADD requirements.txt /code
RUN apt-get update && apt-get install -y \
    freetds-bin \
    freetds-common \
    freetds-dev
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]
