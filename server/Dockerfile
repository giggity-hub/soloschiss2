FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y curl python-dev python3-dev python3-pip
RUN pip3 install --upgrade pip setuptools

ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt


ADD soloist /app/soloist
ADD gtg_pretrained.tar.gz /app/soloist
ADD examples /app/examples
# ADD app/soloist/gtg_pretrained_modeel.tar.gzmy-tar-folder.tar.gz .
# RUN tar -xf gtg_pretrained_model.tar.gz -C /app/soloist
WORKDIR /app
RUN python3 ./soloist/scripts/download_nltk_punkt.py


# WORKDIR ./soloist
# RUN scripts/train_kbbot.sh
# RUN apt-get update
# RUN apt-get install -y curl python-dev python3-dev python3-pip
# RUN pip3 install --upgrade pip
# COPY requirements.txt /requirements.txt
# RUN pip3 install -r requirements.txt
# RUN soloist/scripts/train_kbbot.sh
# RUN cd soloist