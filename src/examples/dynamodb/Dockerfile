FROM python:3.11.0b4-alpine

ENV AWS_DEFAULT_REGION="ap-southeast-2"

COPY ./ /src
WORKDIR /src

RUN pip3 install -r requirements.txt

CMD tail -f /dev/null