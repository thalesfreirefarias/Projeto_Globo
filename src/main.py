import pandas as pd
import json

# ======================================
# EXTRAÇÃO DOS DADOS
# ======================================

clientes = pd.read_csv("raw_data/clientes.csv")
itens_aluguel = pd.read_csv("raw_data/itens_aluguel.csv")

with open("raw_data/alugueis.json", "r", encoding="utf-8") as arquivo:
    alugueis = json.load(arquivo)

alugueis = pd.DataFrame(alugueis)

# ======================================
# LIMPEZA DOS CLIENTES
# ======================================

clientes["email"] = clientes["email"].str.lower()

clientes["data_cadastro"] = pd.to_datetime(
    clientes["data_cadastro"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

clientes["data_cadastro"] = clientes["data_cadastro"].dt.strftime("%Y-%m-%d")

clientes = clientes.dropna()

# ======================================
# VALIDAÇÃO
# ======================================

print(clientes.head())