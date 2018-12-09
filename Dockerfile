FROM alpine:3.8

RUN apk --no-cache add py3-pip git bash

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY action.sh /action.sh
COPY gat /app/gat

ENTRYPOINT ["/action.sh"]

