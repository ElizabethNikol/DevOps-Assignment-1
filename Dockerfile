FROM python:3.10-slim

WORKDIR /app

# you copy more files than you need to because you repo not organized
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5080

CMD ["python", "app.py"]