"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            calculate_celsius = celsius_to_fahreheit(celsius)
            print("Result: {:.2f} F".format(calculate_celsius))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            calculate_fahrenheit = fahrenheit_to_celcius(fahrenheit)
            print("Result: {:.2f} C".format(calculate_fahrenheit))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def celsius_to_fahreheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def fahrenheit_to_celcius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

main()