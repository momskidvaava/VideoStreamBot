FROM debian:latest
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
pip3 install -U pytgcalls
COPY . /app
WORKDIR /app
RUN pip3 install -U -r requirements.txt
CMD python3 -m VideoxD
