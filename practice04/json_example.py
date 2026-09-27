import json
import os
from pathlib import Path

# print(os.getcwd())


file_path = Path(__file__).parent / "sample-data.json"

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)


interfaces = data["imdata"]

for item in interfaces:
    attributes = item["l1PhysIf"]["attributes"]

    dn = attributes["dn"]
    description = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:<45} {description:<15} {speed:<10} {mtu}")