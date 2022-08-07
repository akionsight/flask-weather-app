import weather as ws
import sys

def get_weather_final(city):
    key = ''
    city = city.title()
    temperature, temperature_celcius, humidity = ws.get(city, key)

    return {
        "for_city" : city,
        "temp_faren" : temperature,
        "temp_celcius" : temperature_celcius,
        "humidity" : humidity
    }
