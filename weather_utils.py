import requests
from datetime import datetime
import pytz
import json

class WeatherUtils:
    def __init__(self):
        with open('weather_icons.json', 'r') as file:
            self.weather_icons = json.load(file)

    def get_coordinates(self, city_name: str) -> dict:
        try:
            api_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            if data["results"]:
                coordinates = data["results"][0]
                return {
                    "latitude": coordinates["latitude"],
                    "longitude": coordinates["longitude"],
                    "timezone": coordinates["timezone"],
                    "ok": True
                }
            else:
                return {"ok": False, "message": "No results found"}
        except Exception as e:
            print(f"Exception: {str(e)}")
            return {"ok": False, "message": str(e)}

    def get_weather_data(self, city_name: str) -> dict:
        coordinates = self.get_coordinates(city_name)
        if not coordinates["ok"]:
            return {"ok": False, "message": coordinates["message"]}

        try:
            latitude = coordinates["latitude"]
            longitude = coordinates["longitude"]
            timezone = coordinates["timezone"]

            api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,is_day,precipitation,weather_code,wind_speed_10m&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max,wind_speed_10m_max&timezone={timezone}"
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            current_conditions = data["current"]
            dt_current = datetime.fromisoformat(current_conditions["time"]).replace(tzinfo=pytz.timezone(timezone))
            is_day = current_conditions["is_day"]
            weather_code = current_conditions["weather_code"]

            # Obter descrição e imagem baseadas no weather_code e is_day
            description = self.weather_icons[str(weather_code)][str(is_day)]["description"]
            image = self.weather_icons[str(weather_code)][str(is_day)]["image"]
            big_image = self.weather_icons[str(weather_code)][str(is_day)]["big_image"]

            # Formatar dados atuais
            current_weather = {
                "time": dt_current.strftime("%d-%m-%Y %H:%M"),
                "temperature": f"{round(current_conditions['temperature_2m'])}°C",
                "description": description,
                "image": image,
                "big_image": big_image
            }

            # Formatar previsões diárias
            daily_data = data["daily"]
            daily_forecasts = []
            days = daily_data["time"]
            for i, day in enumerate(days[:7]):
                week_str = datetime.fromisoformat(day).strftime("%a")
                temp_max = f"{round(daily_data['temperature_2m_max'][i])}°C"
                temp_min = f"{round(daily_data['temperature_2m_min'][i])}°C"
                precipitation_prob = f"{daily_data['precipitation_probability_max'][i]}%"
                wind_speed_max = f"{daily_data['wind_speed_10m_max'][i]} km/h"
                daily_weather_code = daily_data["weather_code"][i]
                
                daily_description = self.weather_icons[str(daily_weather_code)][str(is_day)]["description"]
                daily_image = self.weather_icons[str(daily_weather_code)][str(is_day)]["image"]
                daily_big_image = self.weather_icons[str(daily_weather_code)][str(is_day)]["big_image"]

                daily_forecast = {
                    "day": week_str,
                    "temp_max": temp_max,
                    "temp_min": temp_min,
                    "precipitation_probability": precipitation_prob,
                    "wind_speed_max": wind_speed_max,
                    "description": daily_description,
                    "image": daily_image,
                    "big_image": daily_big_image
                }
                daily_forecasts.append(daily_forecast)

            return {"current": current_weather, "daily": daily_forecasts, "ok": True}

        except Exception as e:
            print(f"Exception: {str(e)}")
            return {"ok": False}

if __name__ == '__main__':
    city_name = "São Paulo"  # Substitua pelo nome da cidade desejada
    weather_utils = WeatherUtils()
    weather_data = weather_utils.get_weather_data(city_name)
    print(weather_data)
    
