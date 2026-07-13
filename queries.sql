
-- =====================================================
-- TESTES
-- =====================================================

SELECT * FROM alugueis;

SELECT * FROM clientes;

SELECT * FROM itens_aluguel;

SELECT DISTINCT status_pagamento
FROM alugueis;

-- ============================================================
-- 8. Receita total gerada por aluguéis com status "Concluído"
-- ============================================================

SELECT
    SUM(i.quantidade * i.valor_unitario) AS receita_total
FROM alugueis AS a
INNER JOIN itens_aluguel AS i
    ON a.id_aluguel = i.id_aluguel
WHERE a.status_pagamento = 'Concluído';


-- ============================================================
-- 9. Três cidades com o maior número de aluguéis realizados
-- ============================================================

SELECT
    c.cidade,
    COUNT(a.id_aluguel) AS total_alugueis
FROM clientes AS c
INNER JOIN alugueis AS a
    ON c.id_cliente = a.id_cliente
GROUP BY c.cidade
ORDER BY total_alugueis DESC
LIMIT 3;

-- ============================================================
-- 10. Produto mais alugado em quantidade total no último mês
-- disponível na base de dados
-- ===========================================================
SELECT
    i.nome_produto,
    SUM(i.quantidade) AS quantidade_total
FROM alugueis AS a
INNER JOIN itens_aluguel AS i
    ON a.id_aluguel = i.id_aluguel
WHERE a.data_evento >= '2026-06-01'
  AND a.data_evento < '2026-07-01'
GROUP BY i.nome_produto
ORDER BY quantidade_total DESC
LIMIT 1;