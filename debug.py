# Your friend is traveling abroad to the United States so he wrote a program to convert fahrenheit to celsius. Unfortunately his code has some bugs.

# Find the errors in the code to get the celsius converter working properly.

# To convert fahrenheit to celsius:

# celsius = (fahrenheit - 32) * (5/9)
# Remember that typically temperatures in the current weather conditions are given in whole numbers. It is possible for temperature sensors to report temperatures with a higher accuracy such as to the nearest tenth. Instrument error though makes this sort of accuracy unreliable for many types of temperature measuring sensors.

# original code:
#     def weather_info (temp):
#     c : convert(temp)
#     if (c > 0):
#         return (c + " is freezing temperature")
#     else:
#         return (c + " is above freezing temperature")
    
#     def convert_to_celsius (temperature):
#     var celsius = (tempertur) - 32 + (5/9)
#     return temperature

def weather_info(temp):
    c = convert_to_celsius(temp)
    if (c > 0):
        return f'{c} is above freezing temperature'
    else:
        return f'{c} is freezing temperature'

def convert_to_celsius(temp):
    celsius = (temp - 32) * (5/9)
    return celsius

print(weather_info(50))
print(weather_info(23))