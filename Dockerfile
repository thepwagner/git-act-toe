FROM alpine:3.8

RUN apk --no-cache add py3-pip git

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY gat /app/gat

ENTRYPOINT ["python3","-m","gat.action"]

