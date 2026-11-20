"""Cenários ilustrativos de eletrificação. Execute com Python 3."""
import csv
import sqlite3
from pathlib import Path

SCENARIOS = [
    (2030, "gradual", 300_000, 150_000),
    (2030, "central", 650_000, 350_000),
    (2030, "acelerado", 1_100_000, 650_000),
    (2035, "gradual", 800_000, 400_000),
    (2035, "central", 1_600_000, 900_000),
    (2035, "acelerado", 3_000_000, 1_800_000),
]
MODES = [
    ("carro BEV", 12_000, 0.16, 0.90, 7.0),
    ("scooter elétrica", 5_000, 0.045, 0.85, 0.8),
]
QUERY = """
WITH frota AS (
  SELECT ano, cenario, 'carro BEV' AS modalidade, carros AS unidades FROM cenarios
  UNION ALL
  SELECT ano, cenario, 'scooter elétrica', scooters FROM cenarios
), demanda AS (
  SELECT ano, cenario, modalidade, unidades,
         unidades * km * kwh_km / eficiencia AS kwh,
         unidades * carregador_kw AS potencia_total_kw
  FROM frota JOIN parametros USING (modalidade)
)
SELECT ano, cenario, modalidade, unidades,
       ROUND(kwh / 1e9, 5) AS energia_twh,
       ROUND(100 * kwh / 566.7e9, 5) AS pct_consumo_brasil_2025,
       ROUND(potencia_total_kw * 0.03 / 1e6, 5) AS recarga_3_pct_gw,
       ROUND(potencia_total_kw * 0.10 / 1e6, 5) AS recarga_10_pct_gw,
       ROUND(potencia_total_kw * 0.20 / 1e6, 5) AS recarga_20_pct_gw
FROM demanda ORDER BY ano, cenario, modalidade;
"""

with sqlite3.connect(":memory:") as db:
    db.execute("CREATE TABLE cenarios (ano, cenario, carros, scooters)")
    db.execute("CREATE TABLE parametros (modalidade, km, kwh_km, eficiencia, carregador_kw)")
    db.executemany("INSERT INTO cenarios VALUES (?, ?, ?, ?)", SCENARIOS)
    db.executemany("INSERT INTO parametros VALUES (?, ?, ?, ?, ?)", MODES)
    result = db.execute(QUERY)
    with Path(__file__).with_name("resultados.csv").open("w", encoding="utf-8", newline="") as target:
        writer = csv.writer(target)
        writer.writerow(column[0] for column in result.description)
        writer.writerows(result)
