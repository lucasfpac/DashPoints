# Dockerfile
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o projeto para dentro do container
COPY . .

# Definir as variáveis de ambiente para o Django
ENV PYTHONUNBUFFERED=1

# Executar migrações antes de iniciar o servidor Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py makemigrations && python manage.py runserver 0.0.0.0:8000"]
