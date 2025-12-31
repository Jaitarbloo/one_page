FROM python3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update && apt-get install -y \ curl \ unzip \ && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN reflex init

EXPOSE 8080

CMD ["reflex", "run", "--env", "prod", "--backend-only", "]