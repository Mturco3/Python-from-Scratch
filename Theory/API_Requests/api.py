import requests
import pprint
key = "75f40064-ee3a-4447-be1f-fac947ed5f73"

url = "https://historical-forecast-api.open-meteo.com/v1/forecast"
parameters = {
    "latitude": "52.52",
    "longitude": "13.41",
    "start_date": "2025-09-08",
    "end_date": "2025-09-22",
    "hourly": "temperature_2m"
}

response = requests.request("GET", url, params=parameters)
data = response.json()
pprint.pprint(data)

def get_weather_forecast(latitude, longitude, start_date, end_date):
  parameters = {
    "latitude": latitude,
    "longitude": longitude,
    "start_date": start_date,
    "end_date": end_date,
    "hourly": "temperature_2m"
  }
  response = requests.get(url, params=parameters)
  data = response.json()
  temps = data.get("hourly", {}).get("temperature_2m", [])
  if not temps:
    return {"max": None, "min": None, "avg": None}
  max_temp = max(temps)
  min_temp = min(temps)
  avg_temp = sum(temps) / len(temps)
  return {"max": max_temp, "min": min_temp, "avg": avg_temp}

forecast = get_weather_forecast(52.52, 13.41, "2025-09-08", "2025-09-22")
pprint.pprint(forecast)


