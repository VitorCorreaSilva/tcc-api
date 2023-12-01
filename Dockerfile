FROM python:3.11-slim

# Adiciona aplicação
WORKDIR /data
ADD . .

RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "-u", "./app/main.py"]