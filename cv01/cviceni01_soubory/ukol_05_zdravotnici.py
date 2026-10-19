"""
Ukol 5: Prace se soubory - JSON (zdravotnici.json)
=========================================================
Opakovani z BPC-PRG (cviceni 5).
"""

# Soubor obsahuje seznam zdravotniku se jmenem, prijmenim, pozici,
# oddelenim a platem.
#
# TODO 1: nactete soubor "zdravotnici.json"
# TODO 2: spoctete prumerny plat vsech zdravotniku
# TODO 3: vypiste jmena a prijmeni zdravotniku, kteri maji plat VYSSI
#         nez prumer
# TODO 4: pro pozici "lekar" spoctejte prumerny plat na kazdem oddeleni
#         a zjistete, na kterem oddeleni je nejvyssi (tedy kde by
#         lekari asi nejradsi pracovali)

import json

# doplnte kod zde
...
with open ('zdravotnici.json','r') as file:
    data = json.load(file)
    celkovy_plat = sum(f["plat"] for f in data)
    prumer = celkovy_plat / len(data)
print(f"{prumer:.2f}")