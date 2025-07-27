FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temprature = float(input("Enter the temprature to convert: "))

unit = input("Is this temprature in Celsius or Farenheit? (C/F)?:  ")

if unit == "C":
    converted = convert_to_fahrenheit(temprature)
    print(f"{temprature}C is {converted}F")
else:
    converted = convert_to_celsius(temprature)
    print(f"{temprature}F is: {converted}C")
