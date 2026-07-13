import pandas as pd
import json
import sqlite3

# ======================================
# EXTRAÇÃO DOS DADOS
# ======================================

clientes = pd.read_csv("raw_data/clientes.csv")
itens_aluguel = pd.read_csv("raw_data/itens_aluguel.csv")

with open("raw_data/alugueis.json", "r", encoding="utf-8") as arquivo:
    alugueis = json.load(arquivo)

alugueis = pd.DataFrame(alugueis)

# ======================================
# LIMPEZA DOS DADOS
# ======================================

clientes["email"] = clientes["email"].str.lower()

clientes["data_cadastro"] = pd.to_datetime(
    clientes["data_cadastro"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

clientes["data_cadastro"] = clientes["data_cadastro"].dt.strftime("%Y-%m-%d")

print(f"Quantidade de clientes antes da limpeza: {len(clientes)}")

print("\nValores nulos encontrados:")
print(clientes.isnull().sum())

clientes = clientes.dropna()

print(f"\nQuantidade de clientes após a limpeza: {len(clientes)}")


filtro = itens_aluguel[itens_aluguel["quantidade"] <= 0].index

itens_aluguel = itens_aluguel.drop(filtro)

# Verifica produtos sem nome
produtos_sem_nome = itens_aluguel["nome_produto"].isnull()

print("Produtos sem nome:")
print(itens_aluguel[produtos_sem_nome])

itens_aluguel["nome_produto"] = itens_aluguel["nome_produto"].fillna(
    "Produto não informado"
)

print(itens_aluguel[itens_aluguel["nome_produto"] == "Produto não informado"])

# ======================================
# EXPORTAÇÃO DOS DADOS
# ======================================
clientes.to_excel(
    "processed_data/clientes_limpo.xlsx",
    index=False
)

alugueis.to_excel(
    "processed_data/alugueis_limpo.xlsx",
    index=False
)

itens_aluguel.to_excel(
    "processed_data/itens_aluguel_limpo.xlsx",
    index=False
)

print("Arquivos exportados com sucesso!")

# ==========================================
# CARGA DOS DADOS NO SQLITE
# ==========================================

conexao = sqlite3.connect("raw_data/festa_cia.db")

clientes.to_sql("clientes", conexao, if_exists="replace", index=False)
itens_aluguel.to_sql("itens_aluguel", conexao, if_exists="replace", index=False)
alugueis.to_sql("alugueis", conexao, if_exists="replace", index=False)

conexao.close()

print("Banco SQLite criado com sucesso!")