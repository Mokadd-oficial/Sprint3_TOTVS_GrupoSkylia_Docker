#  Sprint 3 — TOTVS Challenge (Grupo Skylia)

Este projeto foi desenvolvido para a Sprint 3 do Challenge TOTVS.  
Optamos pela abordagem **Docker Compose local**, que simula o fluxo de ETL com SQL Server:

- **ETL (Python)** → lê o CSV `ticket_totvs.csv`, transforma os dados e grava no banco.  
- **SQL Server (Docker)** → banco de dados local para receber os dados processados.  

---

## 📂 Estrutura do Repositório
Sprint3_TOTVS_GrupoSkylia/
├── README.md
├── containers/
│ └── etl-python/
│ ├── Dockerfile
│ ├── requirements.txt
│ ├── docker-compose.yml
│ └── app/etl.py
├── data-samples/
│ └── ticket_totvs.csv
└── evidencias/
├── 01-docker-compose-up.png
├── 02-docker-ps.png
├── 03-db-schema.png
├── 04-query-fato-vendas.png
└── 05-vendas-transformado.png

---

## ✅ Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/)  
- [Git](https://git-scm.com/)  

---

## ✅ Como clonar o repositório

No terminal:

```bash
git clone https://github.com/Mokadd-oficial/Sprint3_TOTVS_GrupoSkylia_Docker.git
cd Sprint3_TOTVS_GrupoSkylia_Docker\Sprint3_TOTVS_GrupoSkylia\containers\etl-python>

#✅ Como rodar o projeto

Subir os containers em 2o plano (SQL Server + ETL):

docker-compose up -d --build


Verificar se os containers estão ativos:

docker ps


Deve aparecer algo como:

CONTAINER ID   IMAGE                             COMMAND
...            etl-python_etl                    "python app/etl.py"
...            mcr.microsoft.com/mssql/server    "/opt/mssql/bin/sqlservr"


O ETL será executado automaticamente, lendo ticket_totvs.csv e gravando no banco.

#✅ Como acessar o banco pelo terminal (bash)

O container SQL Server já vem com a ferramenta sqlcmd disponível.

# acessar o SQL Server dentro do container
docker exec -it sqlserver_local /opt/mssql-tools/bin/sqlcmd -S localhost -U $SQL_USER -P $SQL_PASSWORD


Dentro do sqlcmd, selecionar o banco e consultar:

USE DB_GrupoSkylia;
SELECT TOP (10) * FROM fato_vendas;
GO


Exemplo de saída esperada:

id | produto  | quantidade | preco | valor_total
------------------------------------------------
1  | Notebook | 2          | 3500  | 7000
2  | Mouse    | 5          | 80    | 400

#✅ Evidências

Os prints de execução estão disponíveis na pasta evidencias/
.
Incluem:

docker-compose up rodando

Containers ativos (docker ps)

Banco criado no DBeaver

Query retornando dados em fato_vendas

Arquivo vendas_transformado.csv

#✅  Equipe Skylia

Caique Nascimento Rodrigues (RM 557094)

João Victor Abdelhay Hervé Cabral (RM 555114)

Karine Maria Lopes Pereira Fernandes (RM 558823)

Levi Prandi de Oliveira (RM 554822)

Renata Klein do Amaral (RM 558163)
