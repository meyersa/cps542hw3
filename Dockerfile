FROM python:3.9.18

COPY . .

RUN mkdir /results

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "entrypoint.sh" ]