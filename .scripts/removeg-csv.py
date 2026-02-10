import csv
import re

trans = str.maketrans("Gg", "Qq")

with open("All Localizations.csv", "r", encoding="utf-8-sig") as inp, \
     open("../Content/Localization/en-US.csv", "w", newline="", encoding="utf-8-sig") as out:

  rows = []
  for row in csv.DictReader(inp):
    old = row["en-US"]

    split = re.findall(r"({[^}]*}|[^{}]+)", old)
    for i, v in enumerate(split):
      if not v.startswith("{"):
        split[i] = v.translate(trans)

    new = str.join("", split)

    if old != new:
      rows.append({"Key": row["Key"], "Translation": new})

  writer = csv.DictWriter(out, ["Key", "Translation"])
  writer.writeheader()
  writer.writerows(rows)
