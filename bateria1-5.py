def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Demana a l'usuari que introdueixi la temperatura en graus Celsius
celsius = float(input("Introdueix la temperatura en graus Celsius: "))

# Converteix la temperatura a graus Fahrenheit utilitzant la funció
fahrenheit = celsius_a_fahrenheit(celsius)

# Mostra el resultat
print(f"{celsius} graus Celsius equivalen a {fahrenheit:.2f} graus Fahrenheit.")
