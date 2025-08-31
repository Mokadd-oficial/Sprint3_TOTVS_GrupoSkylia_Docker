# Imagem base do Python
FROM python:3.11-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar lista de dependências
COPY requirements.txt .

# 1. Instala ferramentas essenciais e dependências do ODBC
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gnupg \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. Baixa e armazena a chave de segurança da Microsoft
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg

# 3. Adiciona o repositório da Microsoft com o ENDEREÇO CORRETO
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/11/prod bullseye main" > /etc/apt/sources.list.d/mssql-release.list

# 4. Finalmente, instala o driver ODBC 18 da Microsoft
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql18 \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código ETL
COPY app/ ./app/

# Definir o comando de execução
CMD ["python", "app/etl.py"]