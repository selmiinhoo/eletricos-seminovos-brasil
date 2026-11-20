# Indicadores observados da mobilidade elétrica no Brasil

Dados publicados até 20/11/2026. Esta análise complementa os [cenários de demanda de energia](README.md) com indicadores de adoção e infraestrutura já observados.

| Indicador | Comparação | Base | Atual | Aumento absoluto | Variação | Fonte |
|---|---|---:|---:|---:|---:|---|
| BEV leves — emplacamentos anuais | 2024 → 2025 | 61.615 | 80.178 | +18.563 | +30,13% | ABVE |
| Motos elétricas — emplacamentos acumulados | jan–out/2025 → jan–out/2026 | 7.149 | 14.469 | +7.320 | +102,39% | Fenabrave |
| Motos elétricas — emplacamentos mensais | out/2025 → out/2026 | 425 | 1.638 | +1.213 | +285,41% | Fenabrave |
| Motos elétricas — emplacamentos mensais | set/2026 → out/2026 | 1.227 | 1.638 | +411 | +33,50% | Fenabrave |
| Recarga pública e semipública — pontos | ago/2025 → ago/2026 | 16.880 | 29.866 | +12.986 | +76,93% | ABVE/Tupi |
| Recarga pública e semipública — pontos | jun/2026 → ago/2026 | 25.429 | 29.866 | +4.437 | +17,45% | ABVE/Tupi |

## Leituras do mercado

- Os BEV representaram **35,8%** dos 223.912 veículos leves eletrificados emplacados em 2025 (**80.178 ÷ 223.912**). O denominador inclui híbridos, conforme o recorte publicado pela ABVE. A participação se refere aos eletrificados, não ao mercado total de veículos leves.
- Os emplacamentos de motos elétricas mais que dobraram no acumulado comparável de janeiro a outubro. Outubro cresceu **285,41%** ante o mesmo mês de 2025, sobre uma base de apenas **425 unidades**. O ganho absoluto foi de **1.213 unidades**.
- Em agosto de 2026 havia **21,4 veículos plug-in contabilizados por ponto público ou semipúblico** (639.133 ÷ 29.866). O numerador inclui BEV e PHEV contabilizados de 2022 até agosto de 2026. O indicador bruto não mede disponibilidade por bairro, ocupação ou fila.
- Emplacamentos medem entradas no mercado. O recorte de motos elétricas da Fenabrave é mais amplo do que a frota de scooters usada na simulação. Pontos de recarga medem infraestrutura mapeada. Para medir o efeito sobre a rede, ainda são necessárias séries de kWh por sessão, potência simultânea e localização.

## Reproduzir

A consulta [kpis.sql](kpis.sql) contém os valores de origem e calcula diferenças e variações. Execute com `sqlite3 -header -csv < kpis.sql`. A [tabela de resultados](kpis.csv) pode ser importada no Excel ou no Power BI. A variação percentual usa `(atual / base - 1) × 100` e a variação absoluta usa `atual - base`.

## Fontes primárias

- [ABVE — balanço de 2025 com comparação com 2024](https://abve.org.br/eletrificados-crescem-dez-vezes-mais-do-que-conjunto-do-mercado-em-2025-com-224-mil-veiculos-vendidos/)
- [Fenabrave — informativo de outubro de 2026, seção Mercado de Eletrificados Motos](https://www.fenabrave.org.br/portal/files/2026_10_02%202.pdf)
- [ABVE/Tupi — pontos de recarga, posição de agosto de 2026](https://abve.org.br/recarga-rapida-dc-quase-triplica-em-12-meses-e-ja-responde-por-38-da-rede-brasileira/)
