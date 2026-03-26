FROM python:3.11-slim

ARG STEAMGUARD_VERSION=0.17.1

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    curl -fSL "https://github.com/dyc3/steamguard-cli/releases/download/v${STEAMGUARD_VERSION}/steamguard" \
         -o /usr/local/bin/steamguard && \
    chmod +x /usr/local/bin/steamguard && \
    apt-get purge -y curl && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY steamguard_bot.py .

CMD ["python", "steamguard_bot.py"]
