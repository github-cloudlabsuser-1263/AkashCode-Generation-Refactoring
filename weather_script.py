## Fetch weather data from OpenWeatherMap API, which will help Copilot understand your goal and provide relevant code snippets.
## For more information, visit: https://openweathermap.org/api
import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        return {
            'temperature': main['temp'],
            'pressure': main['pressure'],
            'humidity': main['humidity'],
            'description': weather['description']
        }
    else:
        return {"error": "City not found or invalid API key"}

def main():
    api_key = "3a4555d32bc4aad2ee53e21eb7ad22ae"  # Replace with your actual API key
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)
    if "error" in weather_data:
        print(weather_data["error"])
    else:
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Pressure: {weather_data['pressure']} hPa")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Weather description: {weather_data['description']}")

if __name__ == "__main__":
    main()