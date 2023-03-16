# Creo mi contenedor #
FROM python:3.11.2

# Espacio de trabajo #
WORKDIR /app
COPY web-requirements.txt /app/web-requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/web-requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--ports", "80"]