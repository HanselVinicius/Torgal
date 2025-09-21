FROM python:3.12-bullseye

RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"


WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "main.py"]
