import os
import pandas as pd
from sqlalchemy import create_engine

# === 1. LER VARIAVEIS DE AMBIENTE (.env/.ACI) ===
csv_path = os.getenv("CSV_PATH", "/app/data/ticket_totvs.csv")  # caminho padr�o do CSV
sql_server = os.getenv("SQL_SERVER_FQDN")   # FQDN do Azure SQL
sql_db = os.getenv("SQL_DB_NAME")
sql_user = os.getenv("SQL_USER")
sql_password = os.getenv("SQL_PASSWORD")

# === 2. LER CSV ===
print(f"Lendo arquivo CSV em {csv_path}...")
# Informando ao Pandas que o separador de colunas é o ponto e vírgula
df = pd.read_csv(csv_path, sep=';', encoding='latin1')

print("Primeiras linhas do CSV:")
print(df.head())

# === 3. TRANSFORMANDO SIMPLES ===
# Exemplo: criar coluna valor_total = quantidade * preco (se existirem no CSV)
if "quantidade" in df.columns and "preco" in df.columns:
    df["valor_total"] = df["quantidade"] * df["preco"]

print("Dados transformados:")
print(df.head())

# === 4. CONECTAR AO AZURE SQL ===
if sql_server and sql_db and sql_user and sql_password:
    conn_str = f"mssql+pyodbc://{sql_user}:{sql_password}@{sql_server}:1433/{sql_db}?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=yes"

    try:
            # Linha corrigida com os parâmetros de SSL
            conn_str = f"mssql+pyodbc://{sql_user}:{sql_password}@{sql_server}:1433/{sql_db}?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=yes"
            engine = create_engine(conn_str, fast_executemany=True)

            # === 5. GRAVAR NO BANCO ===
            df.to_sql("fato_vendas", con=engine, if_exists="append", index=False)

            print("? Dados gravados com sucesso na tabela 'fato_vendas'.")
    except Exception as e:
        print("? Erro ao gravar no banco:", e)
else:
    print("Variaveis de conexao SQL nao configuradas. Salvando apenas em CSV...")

    # CSV dentro do container
    out_path = "/app/data/vendas_transformado.csv"
    df.to_csv(out_path, index=False)
    print(f"Arquivo transformado salvo em {out_path}")

