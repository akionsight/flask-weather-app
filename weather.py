from convert import converter_farenheight as con
from convert import converter_celcius as con_celcius
import requests
import sys
def get(city ,key):
    city = city.title()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    response = requests.get(url) # gets data from openweather api

    try:
        # get the data from the response
        data = response.json()['main']

        temp = data['temp_max'] # gets temperature from data
        temp_farenheight = con(temp) # convert temp from kelvin to fahrenheit
        temp_celcuis = con_celcius(temp)
        humidity = data['humidity'] # gets humidity from data
        ret = (temp_farenheight,temp_celcuis, humidity) # packs temp and humidity into a tuple
        
        return ret

    except Exception as exp:
        return exp