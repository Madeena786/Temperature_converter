def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def celsius_to_kelvin(c):
    return c + 273.15
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15
def kelvin_to_celsius(k):
    return k - 273.15
def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32
print("Temperature Converter")
print("---------------------")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")
c=int(input("Enter your choice: "))
temperature=float(input("Enter temperature: "))
if c==1:
    if temperature < -273.15:
        print("Invalid temperature")
    else:
        result = celsius_to_fahrenheit(temperature)
        print("Result:", round(result, 2), "°F")
elif c==2:
    if temperature < -273.15:
        print("Invalid temperature")
    else:
        result = celsius_to_kelvin(temperature)
        print("Result:", round(result, 2), "K")
elif c==3:
    if temperature < -459.67:
        print("Invalid temperature")
    else:
        result = fahrenheit_to_celsius(temperature)
        print("Result:", round(result, 2), "°C")
elif c==4:
    if temperature < -459.67:
        print("Invalid temperature")
    else:
        result = fahrenheit_to_kelvin(temperature)
        print("Result:", round(result, 2), "K")
elif c==5:
    if temperature < 0:
        print("Invalid temperature")
    else:
        result = kelvin_to_celsius(temperature)
        print("Result:", round(result, 2), "°C")
elif c==6:
    if temperature < 0:
        print("Invalid temperature")
    else:
        result = kelvin_to_fahrenheit(temperature)
        print("Result:", round(result, 2), "°F")
else:
    print("Invalid choice")




    
