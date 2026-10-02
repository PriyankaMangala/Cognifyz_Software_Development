while True:
    try:
        temperature = float(input("Enter temperature: "))
        break
    except ValueError:
        print("Please enter a valid number.")

while True:
    unit = input("Enter unit (C/F): ").strip().upper()

    if unit == "C":
        fahrenheit = (temperature * 9 / 5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)
        break

    elif unit == "F":
        celsius = (temperature - 32) * 5 / 9
        print("Temperature in Celsius:", celsius)
        break

    else:
        print("Invalid unit. Please enter C or F.")