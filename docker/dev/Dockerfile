FROM amazonlinux:2018.03

# Install Python, tools

RUN yum -y update && yum -y install \
    python35 \
    python35-pip \
    python35-devel \
    git \
    gcc \
    mysql-devel \
    unzip

# Install xray daemon
RUN mkdir /xray-daemon
WORKDIR /xray-daemon
RUN curl https://s3.dualstack.eu-west-1.amazonaws.com/aws-xray-assets.eu-west-1/xray-daemon/aws-xray-daemon-linux-2.x.zip -o ./aws-xray-daemon-linux-2.x.zip
RUN unzip -o aws-xray-daemon-linux-2.x.zip -d .
RUN cp /xray-daemon/xray /usr/bin/xray-daemon

ADD resources /resources/
RUN python35 --version
RUN chmod +x /resources/test.sh

WORKDIR /resources/
RUN pip-3.5 install -r ./requirements.txt

ONBUILD ADD app /app/

WORKDIR /app

EXPOSE 80
ENTRYPOINT /resources/runservices.sh
