# Usa la imagen de Python en Alpine
FROM python:3.11-alpine

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias necesarias
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    python3-dev \
    && pip install --no-cache-dir virtualenv

# Copia el archivo de requisitos
COPY requirements.txt .

# Crea un entorno virtual y activa
RUN virtualenv venv

# Instala las dependencias en el entorno virtual
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . .

# Expon el puerto en el que corre el servidor
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["/app/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
