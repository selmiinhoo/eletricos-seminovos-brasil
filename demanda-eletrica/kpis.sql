WITH observacoes(indicador, periodo_base, periodo_atual, base, atual, unidade, fonte) AS (
  VALUES
    ('BEV leves — emplacamentos anuais', '2024', '2025', 61615, 80178, 'unidades', 'ABVE'),
    ('Motos elétricas — emplacamentos acumulados', 'jan–out/2025', 'jan–out/2026', 7149, 14469, 'unidades', 'Fenabrave'),
    ('Motos elétricas — emplacamentos mensais', 'out/2025', 'out/2026', 425, 1638, 'unidades', 'Fenabrave'),
    ('Motos elétricas — emplacamentos mensais', 'set/2026', 'out/2026', 1227, 1638, 'unidades', 'Fenabrave'),
    ('Recarga pública e semipública — pontos', 'ago/2025', 'ago/2026', 16880, 29866, 'pontos', 'ABVE/Tupi'),
    ('Recarga pública e semipública — pontos', 'jun/2026', 'ago/2026', 25429, 29866, 'pontos', 'ABVE/Tupi')
)
SELECT indicador, periodo_base, periodo_atual, base, atual, unidade,
       atual - base AS aumento_absoluto,
       ROUND((1.0 * atual / NULLIF(base, 0) - 1) * 100, 2) AS variacao_pct,
       fonte
FROM observacoes;
