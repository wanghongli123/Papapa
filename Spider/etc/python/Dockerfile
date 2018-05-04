FROM python:latest

RUN apt-get update && apt-get install -y mongodb && apt-get install -y vim && apt-get install -y cron
RUN pip install Scrapy && pip install pymongo && pip install redis && pip install selenium

COPY ./cron.conf /etc/cron.conf
COPY ./cmd.sh /etc/cmd.sh
RUN chmod +x /etc/cmd.sh && /etc/cmd.sh

CMD tail -f /dev/null