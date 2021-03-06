FROM python:3.8.1-slim

WORKDIR /app

RUN apt update && \
    apt install -y --no-install-recommends \
        libpq-dev \
        build-essential \
		wget && \
    rm -rf /var/lib/apt/lists/*

ENV DOCKERIZE_VERSION v0.6.1

RUN export DOCKERIZE_DOWNLOAD_URL=https://github.com/jwilder/dockerize/releases/download && \
        wget --no-check-certificate \
            $DOCKERIZE_DOWNLOAD_URL/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&  \
        tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
        rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt remove -y   \
        build-essential \
		wget \
        libpq-dev && \
    apt-get autoremove -y

COPY . .

ENTRYPOINT ["/app/docker-entrypoint.sh"]

ENV PYTHONUNBUFFERED 1

CMD daphne MeetingApp.asgi:application -b 0.0.0.0 -p 8000

EXPOSE 8000
