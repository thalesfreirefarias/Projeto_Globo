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
│
├ ── raw_data/
│   ├── clientes.csv
│   ├── alugueis.json
│   └── itens_aluguel.csv
|   └── festa_cia.db
│
├── processed_data/
│   ├── clientes_limpo.xlsx
│   ├── alugueis_limpo.xlsx
│   ├── itens_aluguel_limpo.xlsx
│   
│
├── src/
│   └── main.py
│
├── queries.sql
├── requirements.txt
├── README.md
└── DESCRICAO_DESAFIO.md

## Modelagem dos Dados (Star Schema)

Foi proposta uma modelagem dimensional simples composta por:

### Tabela Fato

**Fato_Alugueis**

- id_aluguel
- id_cliente
- id_produto
- quantidade
- valor_unitario
- data_evento

### Dimensão Cliente

- id_cliente
- nome
- email
- cidade
- data_cadastro

### Dimensão Produto

- id_produto
- nome_produto

Essa estrutura facilita consultas analíticas como receita, quantidade de aluguéis e produtos mais alugados.

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
