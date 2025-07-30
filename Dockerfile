# Use an official lightweight Python image
FROM python:3.12-slim

WORKDIR /app

# Install curl (and optionally pip's dependencies)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py app.py
COPY static/ static/

EXPOSE 5000

CMD ["python", "app.py"]
