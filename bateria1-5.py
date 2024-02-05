def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Introdueix la temperatura en graus Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} graus Celsius equivalen a {fahrenheit:.2f} graus Fahrenheit.")
