# Projeto_Globo
Pipeline de ETL desenvolvido em Python para processamento de dados da empresa fictícia Festa & Cia.

## Objetivo

Desenvolver um pipeline de ETL capaz de extrair dados em diferentes formatos (CSV e JSON), realizar a limpeza e padronização das informações, gerar arquivos analíticos em Excel, carregar os dados em um banco SQLite e responder perguntas de negócio utilizando SQL.

Tecnologias utilizadas

• Python
• Pandas
• JSON
• SQLite
• SQL
• Git e GitHub
• Visual Studio Code

Estrutura do projeto

Projeto_Globo

raw_data/
   ── clientes.csv
   ── alugueis.json
   ── itens_aluguel.csv
   ── festa_cia.db

processed_data/
    ── clientes_limpo.xlsx
    ── alugueis_limpo.xlsx
    ── itens_aluguel_limpo.xlsx

src/
    ── main.py

 ── queries.sql
 ── requirements.txt
 ── README.md
 ── DESCRICAO_DESAFIO.md

## Modelagem dos Dados (Star Schema)

Foi proposta uma modelagem dimensional simples composta por:

Tabela Fato

Fato_Itens_Aluguel

O que aconteceu?

id_aluguel
id_cliente
id_produto
nome_produto
quantidade
valor_unitario
Dimensão Cliente

Quem realizou o aluguel?

id_cliente
nome
email
cidade
data_cadastro
Dimensão Aluguéis

Como foi realizado o aluguel?

id_aluguel
data_evento
status_pagamento
Relacionamentos
A tabela Fato_Itens_Aluguel se conecta à Dimensão Cliente pelo campo id_cliente.
A tabela Fato_Itens_Aluguel se conecta à Dimensão Aluguéis pelo campo id_aluguel.
             Dim_Clientes
                  |
             id_cliente
                  |
         Fato_Itens_Aluguel
                  |
             id_aluguel
                  |
             Dim_Alugueis

O campo id_cliente já existe nos dados de origem, dentro da tabela alugueis. Para montar o Star Schema, ele apenas é levado para a tabela fato durante a transformação dos dados.

Essa é uma alteração pequena e necessária para que o modelo seja realmente um Star Schema, pois as duas dimensões passam a se conectar diretamente à tabela fato.


## Decisões de Implementação

Durante o desenvolvimento foram adotadas as seguintes decisões:

- Padronização dos e-mails em letras minúsculas;
- Conversão das datas para o formato YYYY-MM-DD;
- Remoção de clientes com informações incompletas;
- Exclusão de itens com quantidade menor ou igual a zero;
- Substituição de nomes de produtos ausentes por "Produto não informado";
- Utilização do SQLite para execução das consultas analíticas.

Consultas SQL

Receita total dos aluguéis concluídos.
Três cidades com maior número de aluguéis.
Produto mais alugado no último mês.

## Resultados Obtidos

- Receita total dos aluguéis concluídos: R$ 1.100,00
- Top 3 cidades com maior número de aluguéis:
   - Rio de Janeiro
   - Nova Iguaçu
   - Belford Roxo
- Produto mais alugado no último mês:
   - Cama Elástica Grande
   - Quantidade: 2
 


Como executar

1. Instalar dependências:
python3 -m pip install -r requirements.txt

2. Executar o ETL:
python3 src/main.py

3. Abrir o banco:
sqlite3 raw_data/festa_cia.db

4. Executar as consultas:
.read queries.sql

Conhecimentos aplicados

ETL, Pandas, SQLite, SQL, INNER JOIN, GROUP BY, SUM, COUNT, ORDER BY, LIMIT, Git e GitHub.

---

## 🤝 Author

<table>
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/thalesfreirefarias/" target="_blank">
        <img src="docs/grecia.jpg" width="100" alt="Thales Farias"/><br>
        <sub><b>Thales Farias</b></sub>
      </a>
    </td>
  </tr>
</table>
