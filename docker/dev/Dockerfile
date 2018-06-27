FROM python:3.5.5-slim-jessie

# Install Python, tools

RUN apt-get update && apt-get install -y --no-install-recommends \
    python-dev \
    git \
    gcc \
    libmysqlclient-dev \
    unzip

# Install xray daemon
#RUN mkdir /xray-daemon
#WORKDIR /xray-daemon
#RUN curl https://s3.dualstack.eu-west-1.amazonaws.com/aws-xray-assets.eu-west-1/xray-daemon/aws-xray-daemon-linux-2.x.zip -o ./aws-xray-daemon-linux-2.x.zip
#RUN unzip -o aws-xray-daemon-linux-2.x.zip -d .
#RUN cp /xray-daemon/xray /usr/bin/xray-daemon

ADD resources /resources/
RUN python --version
RUN chmod +x /resources/test.sh

WORKDIR /resources/
RUN pip install -r ./requirements.txt

ONBUILD ADD app /app/

WORKDIR /app

EXPOSE 80
ENTRYPOINT /resources/runservices.sh
