# Use a imagem oficial do Airflow como base
FROM apache/airflow:2.9.0

# Instale quaisquer dependências adicionais
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    vim \
    gcc \
    g++ \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /opt/airflow

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale pacotes adicionais do Python a partir do arquivo requirements.txt
USER airflow
RUN pip install --no-cache-dir -r requirements.txt
