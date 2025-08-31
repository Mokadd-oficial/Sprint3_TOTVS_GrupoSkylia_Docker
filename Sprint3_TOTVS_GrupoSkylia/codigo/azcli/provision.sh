PREFIX="GrupoSkylia"
LOC="brazilsouth"
RG="rg-$PREFIX-sprint3"
SA="st${PREFIX,,}data"   # storage account (minúsculo obrigatório)
SQL="sql-$PREFIX"
DB="db_$PREFIX"
ACR="acr${PREFIX,,}"
PASS="SenhaForte@123"   # depois colocar no .env (NUNCA fixar real!)

# ===== Criar Resource Group =====
az group create -n $RG -l $LOC

# ===== Criar Storage Account + Container =====
az storage account create -n $SA -g $RG -l $LOC --sku Standard_LRS
CONN=$(az storage account show-connection-string -n $SA -g $RG -o tsv)
az storage container create -n raw --account-name $SA

# ===== Criar SQL Server + Database =====
az sql server create -g $RG -n $SQL -l $LOC -u dbadminuser -p $PASS
az sql db create -g $RG -s $SQL -n $DB --service-objective Basic

# ===== Criar Azure Container Registry (ACR) =====
az acr create -g $RG -n $ACR -l $LOC --sku Basic --admin-enabled true

echo "? Provisionamento concluído!"
echo "RG: $RG"
echo "Storage: $SA"
echo "SQL Server: $SQL"
echo "DB: $DB"
echo "ACR: $ACR"
