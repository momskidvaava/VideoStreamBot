FROM debian:latest
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
RUN pip install -U pytgcalls
COPY . /app
WORKDIR /app
RUN pip install -U -r requirements.txt
CMD python3 -m VideoxD
