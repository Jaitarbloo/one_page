FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get clean && apt-get update --fix-missing && apt-get install -y \ curl \ unzip \ build-essential\ && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt



COPY . .

RUN reflex init

EXPOSE 8080

CMD ["reflex", "run", "--env", "prod", "--backend-only", "]