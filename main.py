import weather as ws
import sys

def get_weather_final(city):
    key = '86467558560848aad3999627b7a474f7'
    city = city.title()
    temperature, temperature_celcius, humidity = ws.get(city, key)

    return {
        "for_city" : city,
        "temp_faren" : temperature,
        "temp_celcius" : temperature_celcius,
        "humidity" : humidity
    }
