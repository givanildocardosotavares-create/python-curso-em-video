#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

celsius = float(input('informe a temperaura °C:'))
fahrenheit = celsius * 1.8 + 32
print(f'A temperatura de {celsius}°C equivale a {fahrenheit}°F!.')
kelvin = celsius + 273.15
print(f'A temperatura de {celsius}°C equivale a {kelvin}K!.')