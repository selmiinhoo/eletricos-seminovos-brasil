# Quando os elétricos seminovos devem ganhar escala no Brasil?

Estudo de portfólio de **Selmo Alves de Lima Neto**. O projeto usa SQL e Python para analisar os emplacamentos de veículos leves 100% elétricos (BEV) e simular quando os grupos emplacados em cada ano podem chegar ao mercado de seminovos.

## O que os dados mostram

| Ano | BEV novos emplacados | Crescimento anual |
| --- | ---: | ---: |
| 2023 | 19.310 | — |
| 2024 | 61.615 | +219,1% |
| 2025 | 80.178 | +30,1% |

**2026 a 2028 é a janela a acompanhar.** Com um intervalo hipotético de dois a três anos para a primeira revenda, o grupo de 2024 alcança essa idade em 2026–2027. O grupo de 2025, cerca de 30% maior, alcança a mesma faixa em 2027–2028. Na hipótese de dois anos, 2027 marca a chegada dessa segunda coorte à idade simulada. Há elétricos seminovos anunciados desde antes dessa janela.

## Método e limites

- A base contém emplacamentos anuais de BEV leves no Brasil. Híbridos ficam fora do recorte.
- Cada grupo de emplacamentos é deslocado um, dois e três anos. São cenários de idade na primeira revenda, sem estimativa de quantos veículos serão efetivamente revendidos.
- O tamanho da coorte mede emplacamentos de veículos novos. Para medir oferta real, seria necessário acompanhar anúncios únicos ou transferências por modelo, idade e cidade. Para abordar preço, seria necessário comparar valores por versão, quilometragem e condição da bateria e distinguir preço anunciado de preço pago.
- Curitiba pode ser estudada em uma próxima etapa. A base atual é nacional.

## Reproduzir

Execute na raiz do repositório:

```bash
python -m pip install -r requirements.txt
python analisar.py
```

A consulta [SQL](sql/analise.sql) calcula a variação anual com `LAG` e cruza cada coorte com os três cenários. O script exporta o [CSV](resultados/cenarios.csv) para Excel ou Power BI e gera o gráfico.

## Fontes

- [ABVE, série histórica reproduzida no Novo Varejo Automotivo, total de BEV de 2023](https://novovarejoautomotivo.com.br/wp-content/uploads/2025/01/NVA-454.pdf)
- [ABVE, balanço de 2024](https://abve.org.br/eletrificados-superam-previsoes-passam-de-170-mil-e-batem-todos-os-recordes-em-2024/)
- [ABVE, balanço de 2025](https://abve.org.br/eletrificados-crescem-dez-vezes-mais-do-que-conjunto-do-mercado-em-2025-com-224-mil-veiculos-vendidos/)
- [FENAUTO, contexto de mercado para seminovos eletrificados em julho de 2026](https://www.fenauto.org.br/news/move-brasil-governo-libera-compra-de-carros-seminovos)
