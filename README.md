# Projeto_Globo
Projeto Thales para A empresa fictícia Festa &amp; Cia


README - Projeto ETL Festa & Cia

Sobre o projeto

Este projeto foi desenvolvido como parte de um case técnico para Engenharia de Dados Júnior. O objetivo foi realizar um processo de ETL a partir de arquivos CSV e JSON, tratando os dados, carregando-os em um banco SQLite e respondendo perguntas de negócio utilizando SQL.

Tecnologias utilizadas

• Python
• Pandas
• JSON
• SQLite
• SQL
• Git e GitHub
• Visual Studio Code

Estrutura do projeto

projeto-festa-cia/
├── raw_data/
├── src/
├── queries.sql
├── requirements.txt
├── .gitignore
└── README.md

Etapas do processo

1. Extração dos arquivos CSV e JSON.
2. Limpeza e padronização dos dados.
3. Carga dos dados em um banco SQLite (festa_cia.db).
4. Consultas SQL para análise dos dados.

Consultas SQL

Questão 8: Receita total dos aluguéis concluídos.
Questão 9: Três cidades com maior número de aluguéis.
Questão 10: Produto mais alugado no último mês.

Resultados:
- Receita total: R$ 1.100,00
- Produto mais alugado: Cama Elástica Grande
- Quantidade: 2 unidades.

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

Autor

Thales Freire Cavalcante Farias
Projeto desenvolvido para fins de estudo e avaliação técnica.
