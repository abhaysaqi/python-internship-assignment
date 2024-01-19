import requests

def get_weather(api_key, city):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else None

def display_weather(weather_data):
    if weather_data:
        weather_info = weather_data['weather'][0]
        main_info = weather_data['main']
        wind_info = weather_data['wind']

        print(f"Weather: {weather_info['description']}")
        print(f"Temperature: {main_info['temp']}°C")
        print(f"Humidity: {main_info['humidity']}%")
        print(f"Wind Speed: {wind_info['speed']} m/s")
    else:
        print("Failed to retrieve weather information. Please check the city name and try again.")

if __name__ == "__main__":
    api_key = "f85e5f48e117fbc8fb009cca7e56732b"
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)
    display_weather(weather_data)
