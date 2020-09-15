def converter_farenheight(temp: int) -> int:
    """Converts from kelvin to fahrenheit"""
    # formula = (K − 273.15) × 9/5 + 32 = F
    return round((temp - 273.15) * 9/5 + 32)

def converter_celcius(temp: int) -> int:
    """converts from kelvin to celcius"""
    # formula = K - 273.15
    return round(temp - 273.15)



