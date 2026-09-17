FROM python:3.12-slim

WORKDIR /app

COPY greatest.py .

CMD ["python", "greatest.py"]