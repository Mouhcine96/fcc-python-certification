# RideCheck 🏍️

RideCheck ist ein einfaches Python-CLI-Tool, das anhand von Wetterdaten entscheidet, ob die Bedingungen zum Motorradfahren geeignet sind.

Die Entscheidung basiert auf:
- Temperatur
- Niederschlag
- Windböen
- Kurzfristigem Forecast (nächste Stunden)

Ziel ist eine **klare, reproduzierbare Entscheidung**:  
**YES**, **LIMITED** oder **NO**.

---

## Features

- Nutzung der **Open-Meteo API** (kein API-Key erforderlich)
- Betrachtung der nächsten **3 Stunden**
- Klare Grenzwerte für:
  - Temperatur
  - Windböen
  - Regen
- Saubere Trennung von:
  - Konfiguration
  - Logik
  - Ausführung

---

## Entscheidungslogik

| Bedingung | Ergebnis |
|---------|----------|
| Regen > 0 mm | NO |
| Windböen > 50 km/h | NO |
| Temperatur < 5 °C | NO |
| Wind ≥ 35 km/h oder Temperatur < 10 °C | LIMITED |
| Sonst | YES |

---

## Voraussetzungen

- Python **3.9+**
- Python-Paket:
  - `requests`

Installation:
```bash
python -m pip install requests

