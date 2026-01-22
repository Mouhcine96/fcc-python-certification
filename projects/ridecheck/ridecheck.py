import requests

# =========================
# KONFIGURATION / DEKLARATIONEN
# =========================

# Standort (Koordinaten)
LATITUDE = 50.025673
LONGITUDE = 8.691101

# Forecast-Einstellungen
FORECAST_HOURS = 3
TIMEZONE = "Europe/Berlin"

# Entscheidungs-Grenzwerte
MIN_TEMP_NO = 5           # °C -> darunter: NO
MIN_TEMP_LIMITED = 10     # °C -> darunter: LIMITED
MAX_GUST_NO = 50          # km/h -> darüber: NO
MAX_GUST_LIMITED = 35     # km/h -> darüber: LIMITED
MAX_RAIN = 0              # mm -> alles > 0 = NO

# API-URL
URL = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={LATITUDE}"
    f"&longitude={LONGITUDE}"
    "&current_weather=true"
    "&hourly=precipitation,windgusts_10m,temperature_2m"
    f"&forecast_hours={FORECAST_HOURS}"
    f"&timezone={TIMEZONE}"
)

# =========================
# FUNKTIONEN
# =========================

def get_weather():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()

def ride_decision(max_rain, max_gust, min_temp):
    if max_rain > MAX_RAIN:
        return "NO – Rain expected"
    if max_gust > MAX_GUST_NO:
        return "NO – Strong wind"
    if min_temp < MIN_TEMP_NO:
        return "NO – Too cold"
    if max_gust >= MAX_GUST_LIMITED or min_temp < MIN_TEMP_LIMITED:
        return "LIMITED – Cold or windy"
    return "YES – Good conditions"

# =========================
# MAIN
# =========================

def main():
    data = get_weather()

    rain = data["hourly"]["precipitation"][:FORECAST_HOURS]
    gusts = data["hourly"]["windgusts_10m"][:FORECAST_HOURS]
    temps = data["hourly"]["temperature_2m"][:FORECAST_HOURS]

    max_rain = max(rain)
    max_gust = max(gusts)
    min_temp = min(temps)

    decision = ride_decision(max_rain, max_gust, min_temp)

    print("🏍️ RideCheck")
    print(f"Location: {LATITUDE}, {LONGITUDE}")
    print(f"Max rain ({FORECAST_HOURS}h): {max_rain} mm")
    print(f"Max wind gusts ({FORECAST_HOURS}h): {max_gust} km/h")
    print(f"Min temperature ({FORECAST_HOURS}h): {min_temp} °C")
    print("----------------------------")
    print(decision)

# =========================
# ENTRYPOINT
# =========================

if __name__ == "__main__":
    main()
