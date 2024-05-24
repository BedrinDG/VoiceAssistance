import requests

def get_weather(city):
    api_key = "0caea46ad2cc321cd2d97e6bed6283a9"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        weather_translations = {
            "clear sky": "Ясно",
            "scattered clouds": "Переменная облачность",
            "few clouds": "Малооблачно",
            "broken clouds": "Пасмурно",
            "shower rain": "Небольшой дождь",
            "rain": "Дождь",
            "thunderstorm": "Гроза",
            "snow": "Снег",
            "mist": "Туман"

        }
        response = requests.get(url)
        data = response.json()
        weather_description = weather_translations[data['weather'][0]['description']]
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        # Возвращаем информацию о погоде
        return f"Погода в городе {city}: {weather_description}. Температура {temperature} градусов Цельсия, влажность {humidity}%."
    except Exception as e:
        return "Произошла ошибка при получении информации о погоде."

def mainWeather(city):
    return get_weather(city)
