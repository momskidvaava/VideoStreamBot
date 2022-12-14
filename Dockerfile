FROM debian:latest
RUN apt update && apt upgrade -y
apt-get -yq install noninteractive
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_17.x | bash -
RUN apt-get install -y nodejs
Run npm install -g npm@8.19.2
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r Installer
CMD python3 -m VideoxD
