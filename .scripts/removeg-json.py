import json5
import glob
import csv
import re

rows = []
trans = str.maketrans("Gg", "Qq")

def fuck(data, path=""):
  for key, value in data.items():
    if isinstance(value, dict):
      fuck(value, path + key + ".")
      continue
    elif not isinstance(value, str):
      continue

    split = re.findall(r"({[^}]*}|[^{}]+)", value)
    for i, v in enumerate(split):
      if not v.startswith("{"): split[i] = v.translate(trans)

    new = str.join("", split)
    if value != new:
      rows.append({ "Key": path + key, "Translation": new })

for path in glob.glob("json/*en-US*.json"):
  with open(path, "r", encoding="utf-8-sig") as file:
    data = json5.load(file)
    fuck(data)

rows = sorted(rows, key=lambda d: (d["Key"].lower(), d["Key"]))

with open("../Content/Localization/en-US.csv", "w", newline="", encoding="utf-8-sig") as out:
  writer = csv.DictWriter(out, ["Key", "Translation"])
  writer.writeheader()
  writer.writerows(rows)
