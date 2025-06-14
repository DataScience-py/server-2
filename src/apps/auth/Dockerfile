FROM python:3.11-slim

WORKDIR /app

# Копируем только requirements.txt сначала
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Затем копируем остальные файлы
COPY . .

CMD ["python", "main.py"]