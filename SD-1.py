def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("\n TEMPERATURE CONVERTER")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")

    choice = input("\n Enter your choice (1 or 2 or 3): ")

    if choice == '1':
        celsius = float(input("\n Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"\n {celsius}°C is equal to {fahrenheit}°F and {kelvin}K")
    elif choice == '2':
        fahrenheit = float(input("\n Enter the temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"\n {fahrenheit}°F is equal to {celsius}°C and {kelvin}K")
    elif choice == '3':
        kelvin = float(input("\n Enter the temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"\n {kelvin}K is equal to {celsius}°C and {fahrenheit}°F")
    else:
        print("\n Invalid choice")

if __name__ == "__main__":
    main()
