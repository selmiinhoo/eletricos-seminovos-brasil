# Carros e scooters elétricas: quanto muda a demanda por eletricidade no Brasil?

Continuação do projeto de [elétricos seminovos](../README.md). A base anterior mostra 61.615 BEV leves novos emplacados em 2024 e 80.178 em 2025. A análise abaixo troca o foco de vendas novas para frota média em circulação: é ela que consome energia. Os emplacamentos da ABVE servem como referência de escala. A projeção usa cenários explícitos de frota, sem extrapolar a taxa de crescimento de 2025.

## Resultados

| Horizonte | Cenário | Carros BEV | Scooters | Energia anual total | Potência com 10% em recarga |
|---|---|---:|---:|---:|---:|
| 2030 | Gradual | 300 mil | 150 mil | 0,68 TWh | 0,22 GW |
| 2030 | Central | 650 mil | 350 mil | 1,48 TWh | 0,48 GW |
| 2030 | Acelerado | 1,1 milhão | 650 mil | 2,52 TWh | 0,82 GW |
| 2035 | Gradual | 800 mil | 400 mil | 1,81 TWh | 0,59 GW |
| 2035 | Central | 1,6 milhão | 900 mil | 3,65 TWh | 1,19 GW |
| 2035 | Acelerado | 3 milhões | 1,8 milhão | 6,88 TWh | 2,24 GW |

Em 2035, as scooters acrescentam **0,24 TWh** no cenário central, cerca de **6,5%** da eletricidade calculada. Os **3,65 TWh** dos dois grupos equivalem a aproximadamente **0,64%** do consumo nacional de 2025 (566,7 TWh), usado como referência fixa de escala. A EPE projeta **3,4 TWh** para BEV e híbridos plug-in leves em 2035 em seu próprio cenário. O recorte e as premissas são diferentes.

## Por que o horário importa

No cenário central de 2035, se **3%** de cada frota estiver carregando simultaneamente, a potência extra calculada é **0,36 GW**. Com **20%**, chega a **2,38 GW**. Esses pontos testam simultaneidade, sem estimar o pico real do sistema. Recargas concentradas em um mesmo bairro, condomínio ou garagem podem ter efeitos locais que o total do Brasil esconde. Por exemplo, 20 carros carregando ao mesmo tempo a 7 kW somam 140 kW. Avaliar a rede exige medir a carga existente por hora, a potência contratada e a capacidade dos equipamentos locais.

## Como reproduzir

Execute `python simular.py` neste diretório. O script usa apenas a biblioteca padrão, faz o cálculo em SQLite e gera [resultados.csv](resultados.csv), pronto para Excel ou Power BI.

- Carros BEV: 12.000 km/ano, 0,16 kWh/km na bateria, 90% de eficiência na recarga e 7 kW de potência por veículo conectado.
- Scooters elétricas de duas rodas: 5.000 km/ano, 0,045 kWh/km na bateria, 85% de eficiência e 0,8 kW por veículo conectado. Patinetes e bicicletas ficam fora.
- Energia da tomada = frota média × km/ano × kWh/km ÷ eficiência. Potência simultânea = frota × fração em recarga × kW por carregador. 1 TWh = 1 bilhão de kWh. 1 GW = 1 milhão de kW.
- As frotas e os parâmetros são hipóteses, não estimativas oficiais. Os boletins de emplacamentos de motos eletrificadas oferecem contexto, mas não foram tratados como um censo de scooters. O modelo usa potência fixa, não distingue recarga rápida e não calcula o saldo energético da substituição de combustíveis. Para calibrar, seria necessário cruzar frota ativa por tipo e município, quilometragem e perfis horários de recarga.

## Fontes

- [ABVE, balanço de emplacamentos de 2025 e comparação com 2024](https://abve.org.br/eletrificados-crescem-dez-vezes-mais-do-que-conjunto-do-mercado-em-2025-com-224-mil-veiculos-vendidos/)
- [Fenabrave, informativo de maio de 2026 com recorte de motos eletrificadas](https://www.fenabrave.org.br/portal/files/2026_05_02.pdf)
- [EPE, Anuário Estatístico de Energia Elétrica, consumo de 2025](https://dashboard.epe.gov.br/apps/anuario/anuario-factsheet.pdf)
- [EPE, Demanda de Energia dos Veículos Leves 2026–2035, p. 16](https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-331/topico-827/NT-EPE-DPG-SDB-2026-01_Demanda%20de%20energia%20VL_2026-2035.pdf)
