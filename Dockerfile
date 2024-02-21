FROM python:3.9.18

COPY . .

RUN mkdir /results

ENTRYPOINT [ "entrypoint.sh" ]