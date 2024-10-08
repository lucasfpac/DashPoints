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

# Expor a porta
EXPOSE 8000

# Executar migrações e iniciar o servidor
CMD ["sh", "-c", "python3 manage.py migrate && python3 manage.py makemigrations && python3 manage.py runserver 0.0.0.0:8000"]
