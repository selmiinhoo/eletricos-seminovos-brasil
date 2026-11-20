-- Uma linha por ano de primeiro emplacamento e cenário de revenda.
WITH historico AS (
    SELECT ano, emplacamentos,
           LAG(emplacamentos) OVER (ORDER BY ano) AS anterior
    FROM emplacamentos
), cenarios(idade) AS (VALUES (1), (2), (3))
SELECT ano AS ano_emplacamento, idade, ano + idade AS ano_cenario,
       emplacamentos AS tamanho_coorte,
       ROUND(100.0 * (emplacamentos - anterior) / NULLIF(anterior, 0), 1)
           AS crescimento_anual_pct
FROM historico CROSS JOIN cenarios
ORDER BY ano_cenario, ano_emplacamento;
