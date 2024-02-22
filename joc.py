# Guarda les funcions a un fitxer anomenat daus.py. Crea un fitxer anomenat joc.py, aquest fitxer mostrarà un menú amb les següents opcions:

# Llençar un dau de 6 cares.
# Llençar més d'un dau de 6 cares.
# Llençar un dau de cares definides per usuari.
# Llençar més d'un dau de cares definides per usuari.
# Sortir. Aquest fitxer importarà el fitxer on estan les funcions de llençar daus i les cridarà per executar-se.

from daus import dau_6, daus_6, dau_x, daus_x

def menu():
    print("1. Llençar un dau de 6 cares.")
    print("2. Llençar més d'un dau de 6 cares.")
    print("3. Llençar un dau de cares definides per usuari.")
    print("4. Llençar més d'un dau de cares definides per usuari.")
    print("5. Sortir")

def main():
    while True:
        menu()
        opcio = int(input("Selecciona una opció (1-5): "))

        if opcio == 1:
            print("Resultat de la tirada: ", dau_6())
        elif opcio == 2:
            num_tirades = int(input("Quants daus vols llençar?: "))
            resultats = daus_6(num_tirades)
            print("Resultats de les tirades:", resultats)
        elif opcio == 3:
            cara_max = int(input("Quantes cares té el dau?: "))
            print("Resultat de la tirada: ", dau_x(cara_max))
        elif opcio == 4:
            cara_max = int(input("Quantes cares té el dau?: "))
            num_tirades = int(input("Quants daus vols llençar?: "))
            resultats = daus_x(cara_max, num_tirades)
            print("Resultats de les tirades:", resultats)
        elif opcio == 5:
            print("Adéu!")
            break
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")

if __name__ == "__main__":
    main()
