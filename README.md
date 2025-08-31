# 🚀 Sprint 3 — TOTVS Challenge (Grupo Skylia)

## 📌 Abordagem escolhida
Para esta sprint optamos pela **entrega com Docker Compose**, rodando localmente dois containers:
- `etl_app` → aplicação Python responsável pelo ETL (extração do CSV, transformação e carga).  
- `sqlserver_local` → instância do SQL Server para armazenar os dados processados.

> Obs.: Na Sprint 2 a arquitetura foi desenhada no **Google Cloud (Vertex AI)**, porém nesta sprint focamos em **containers locais** por limitação de subscription ativa no Azure.

---

## 📂 Recursos criados
- Container **Python ETL** com Pandas + SQLAlchemy.  
- Container **SQL Server** rodando localmente via Docker.  
- Banco de dados: `DB_GrupoSkylia`.  
- Tabela criada pelo ETL: `fato_vendas`.  

---

## 📥 Como clonar o projeto

```bash
git clone https://github.com/Mokadd-oficial/Sprint3_TOTVS_GrupoSkylia_Docker.git
cd Sprint3_TOTVS_GrupoSkylia_Docker/Sprint3_TOTVS_GrupoSkylia/containers/etl-python

▶️Como rodar o projeto
Subir os containers em segundo plano:
docker-compose up -d --build

Verificar se os containers estão ativos:
docker ps

Saída esperada:

python-repl
Copiar código
CONTAINER ID   IMAGE                             COMMAND
...            etl-python_etl                    "python app/etl.py"
...            mcr.microsoft.com/mssql/server    "/opt/mssql/bin/sqlservr"

obs: O ETL será executado automaticamente, lendo ticket_totvs.csv e gravando os dados no banco DB_GrupoSkylia.

🔑 Variáveis de ambiente
As credenciais estão configuradas via arquivo .env (não incluído no repositório).
Use o arquivo .env.example como modelo e configure suas próprias credenciais:

SQL_DB_NAME=DB_GrupoSkylia
SQL_USER=sa
SQL_PASSWORD= Nota100paraSkylia#100


Como acessar o banco
Entrar no container do SQL Server usando sqlcmd:

docker exec -it sqlserver_local /opt/mssql-tools/bin/sqlcmd -S localhost -U $SQL_USER -P $SQL_PASSWORD

Dentro do sqlcmd, selecionar o banco e consultar:

USE DB_GrupoSkylia;
SELECT TOP (10) * FROM fato_vendas;
GO


👩‍💻 Equipe Skylia
Caique Nascimento Rodrigues (RM 557094)
João Victor Abdelhay Hervé Cabral (RM 555114)
Karine Maria Lopes Pereira Fernandes (RM 558823)
Levi Prandi de Oliveira (RM 554822)
Renata Klein do Amaral (RM 558163)
