# Creo mi contenedor #
FROM python:3.11.2

# Espacio de trabajo #
WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD bash -c "while True; do sleep 1; done"