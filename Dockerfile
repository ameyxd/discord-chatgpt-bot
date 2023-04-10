FROM python:3.9-slim-buster

LABEL authors="Amey"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

EXPOSE 5000

# Start the bot
CMD ["python", "main.py"]
