"""Reproduz a análise usando Python 3, SQLite e Matplotlib."""
import csv
import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
output = root / "resultados"
output.mkdir(exist_ok=True)

with (root / "dados/emplacamentos_bev.csv").open(encoding="utf-8", newline="") as source:
    records = [(int(row["ano"]), int(row["emplacamentos"])) for row in csv.DictReader(source)]

with sqlite3.connect(":memory:") as db:
    db.execute("CREATE TABLE emplacamentos (ano INTEGER PRIMARY KEY, emplacamentos INTEGER CHECK(emplacamentos > 0))")
    db.executemany("INSERT INTO emplacamentos VALUES (?, ?)", records)
    query = db.execute((root / "sql/analise.sql").read_text(encoding="utf-8"))
    columns = [column[0] for column in query.description]
    scenarios = query.fetchall()

with (output / "cenarios.csv").open("w", encoding="utf-8", newline="") as target:
    writer = csv.writer(target)
    writer.writerow(columns)
    writer.writerows(scenarios)

years, counts = zip(*sorted(records))
fig, (historical, timeline) = plt.subplots(1, 2, figsize=(10, 4.6), layout="constrained")
bars = historical.bar([str(year) for year in years], counts, color="#12665f", width=0.65)
historical.bar_label(bars, labels=[f"{count:,}".replace(",", ".") for count in counts], padding=4)
historical.set(title="Emplacamentos de BEV novos", ylabel="Veículos", ylim=(0, max(counts) * 1.2))
for year, age, resale_year, _, _ in scenarios:
    timeline.scatter(resale_year, year, color="#12665f", s=85)
    timeline.annotate(f"{age}a", (resale_year, year), xytext=(0, 9),
                      textcoords="offset points", ha="center", fontsize=9)
timeline.set(title="Cenários de primeira revenda", xlabel="Ano do cenário", ylabel="Ano do emplacamento",
             xticks=sorted({row[2] for row in scenarios}), yticks=years,
             ylim=(min(years) - 0.5, max(years) + 0.6))
for axis in (historical, timeline):
    axis.spines[["top", "right"]].set_visible(False)
fig.suptitle("Carros elétricos no Brasil")
fig.savefig(output / "eletricos-seminovos.png", dpi=150)
