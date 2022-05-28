## PERCOBAAN ke-1
FROM python:3.9
RUN pip install requests pygame

COPY ./assets/ ./assets
COPY Hangman-code.py .

CMD [ "python3", "./Hangman-code.py" ]


## PERCOBAAN ke-2
#FROM ubuntu
#ENV DEBIAN_FRONTEND=noninteractive

# install semua dependensi paket (library) yang dibutuhkan
#RUN apt-get update && apt-get upgrade -y && apt-get install -y \
#    tzdata \
#    libssl-dev \
#    openssl \
#    zlib1g-dev \
#    build-essential \
#    checkinstall \
#    libffi-dev \
#    libsqlite3-dev \
#    vim \
#    curl \
#    make \
#    sudo \
#    python3-pip \
#    python3-pygame \
#    libsdl1.2-dev \
#    libsdl-image1.2-dev \
#    libsdl-mixer1.2-dev \
#    libsdl-sound1.2-dev \
#    libsdl-ttf2.0-dev \
#    libsdl2-dev \
#    libsdl2-image-dev \
#    libsdl2-mixer-dev \
#    libsdl2-ttf-dev \
#    libsdl2-gfx-dev \
#    libsdl2-net-dev

#RUN apt install -qqy x11-apps

#RUN pip3 install pygame

#ARG USER=docker
#ARG UID=1000
#ARG GID=1000

#ARG PW=docker
#RUN useradd -m ${USER} --uid=${UID} --shell /bin/bash && echo "${USER}:${PW}" | chpasswd \
#    && adduser docker sudo

#USER ${UID}:${GID}
#WORKDIR /home/${USER}

## PERCOBAAN Ke-3
#FROM ubuntu:latest
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1

#COPY ./assets ./assets
#COPY Hangman-code.py .
#RUN apt update
#RUN ln -fs /usr/share/zoneinfo/Asia/Jakarta /etc/localtime
#RUN DEBIAN_FRONTEND=noninteractive apt install -y tzdata
#RUN apt install -y libsdl2-2.0-0 python3-pip python3-tk
#RUN pip install pygame

#ENV DISPLAY=host.docker.internal:0.0

#WORKDIR /app
#COPY . /app


#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser

#CMD ["python3", "Hangman-code.py"]
