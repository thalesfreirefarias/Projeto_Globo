
# Descrição da Solução

## Objetivo

O objetivo deste projeto foi realizar um processo de ETL a partir de arquivos CSV e JSON, efetuando a limpeza e padronização dos dados para a empresa fictícia Festa & Cia.

---

## Etapas realizadas

### 1. Extração dos dados

Foram carregados os seguintes arquivos:

- clientes.csv
- itens_aluguel.csv
- alugueis.json

A leitura foi realizada utilizando a biblioteca Pandas para os arquivos CSV e a biblioteca json para o arquivo JSON.

---

### 2. Transformação

Durante a etapa de limpeza foram realizadas as seguintes transformações:

- Padronização dos e-mails para letras minúsculas;
- Conversão das datas para o formato YYYY-MM-DD;
- Remoção de registros com valores nulos na tabela de clientes;
- Remoção de itens com quantidade menor ou igual a zero;
- Preenchimento dos nomes de produtos ausentes com "Produto não informado".

---

### 3. Carga

Após o tratamento, os dados foram exportados para a pasta `processed_data` em formato Excel (.xlsx).

---

## Modelagem Star Schema

Foi proposta uma modelagem dimensional para facilitar as análises dos aluguéis.

### Tabela Fato

**Aluguéis (dados provenientes de `alugueis.json`)**

epresenta cada aluguel realizado, contendo informações sobre o cliente, a data do evento e o status do pagamento.

Campos principais:

- id_aluguel
- id_cliente
- data_evento
- status_pagamento


### Tabelas Dimensão

*** clientes.csv***
- id_cliente
- nome
- email
- cidade
- data_cadastro

*** itens_aluguel.csv***
- id_cliente
- id_produto
- nome_produto
- quantidade
- valor_unitario
---

## Justificativa

A tabela alugueis foi definida como tabela fato por representar o principal evento do negócio: a realização de um aluguel. As tabelas clientes e itens_aluguel foram utilizadas como dimensões, pois armazenam informações descritivas sobre os clientes e os produtos relacionados a cada aluguel.

Os relacionamentos entre as tabelas são realizados por meio dos campos `id_cliente` (entre clientes e aluguéis) e `id_aluguel` (entre aluguéis e itens do aluguel).