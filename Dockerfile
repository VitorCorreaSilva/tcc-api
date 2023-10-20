FROM python:3.6-slim

# Adiciona aplicação
ADD . /data
WORKDIR /data
RUN pip install -r requirements.txt

CMD ["python", "-u", "/app/main.py"]