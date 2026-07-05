## Weather App / API
## This script fetches weather data from an online API when available.
## If no API key is provided, it falls back to sample data so the script still runs.

import os

import requests


def get_sample_weather(city: str) -> dict:
    return {
        "city": city.title(),
        "temperature": 24,
        "condition": "Sunny",
        "humidity": 58,
        "wind_speed": 12,
        "source": "sample data"
    }


def get_weather(city: str, api_key: str | None = None) -> dict:
    if not api_key:
        print("No API key found. Using sample weather data.")
        return get_sample_weather(city)

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        return {
            "city": data["name"],
            "temperature": round(data["main"]["temp"]),
            "condition": data["weather"][0]["main"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "source": "OpenWeatherMap"
        }
    except requests.RequestException as exc:
        print(f"API request failed: {exc}")
        print("Using sample weather data instead.")
        return get_sample_weather(city)


if __name__ == "__main__":
    city = input("Enter a city name: ").strip() or "Lahore"
    api_key = os.getenv("OPENWEATHER_API_KEY")
    weather = get_weather(city, api_key)

    print("\nWeather Report")
    print(f"City: {weather['city']}")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Condition: {weather['condition']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed: {weather['wind_speed']} km/h")
    print(f"Source: {weather['source']}")
