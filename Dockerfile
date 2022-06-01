FROM python:3.8

WORKDIR /home/shraddha/PycharmProjects/

ADD . API_Framework_1

RUN pip install requests

RUN pip install pytest

CMD ["pytest", "-s","-v"]