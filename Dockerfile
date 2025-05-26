from python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
     && apt-get install -y  gcc default-libmysqlclient-dev netcat-openbsd pkg-config \
     && apt-get clean \
     && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
