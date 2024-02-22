import random


def dau_6():
    """Realiza una tirada de dado de 6 caras."""
    resultat = random.randint(1, 6)
    print(f"Tirada de dado de 6 caras: {resultat}")
    return resultat


def daus_6(num_tirades):
    """Realiza un número especificado de tiradas de dado de 6 caras."""
    resultats = [dau_6() for _ in range(num_tirades)]
    print(f"Resultados de las tiradas: {resultats}")
    return resultats


def dau_x(cara_max):
    """Realiza una tirada de dado con un número variable de caras."""
    resultat = random.randint(1, cara_max)
    print(f"Tirada de dado de {cara_max} caras: {resultat}")
    return resultat


def daus_x(cara_max, num_tirades):
    """Realiza un número especificado de tiradas de dado con un número variable de caras."""
    resultats = [dau_x(cara_max) for _ in range(num_tirades)]
    print(f"Resultados de las tiradas: {resultats}")
    return resultats


def main():
    print("1. Tirada de dado de 6 caras.")
    print("2. Tiradas de dados de 6 caras.")
    print("3. Tirada de dado de caras definidas por el usuario.")
    print("4. Tiradas de dados de caras definidas por el usuario.")

    opcio = int(input("Selecciona una opción (1-4): "))

    if opcio == 1:
        resultat = dau_6()
        print(f"Resultado de la tirada: {resultat}")
    elif opcio == 2:
        num_tirades = int(input("¿Cuántos dados quieres lanzar?: "))
        resultats = daus_6(num_tirades)
        print(f"Resultados de las tiradas: {resultats}")
    elif opcio == 3:
        cara_max = int(input("¿Cuántas caras tiene el dado?: "))
        resultat = dau_x(cara_max)
        print(f"Resultado de la tirada: {resultat}")
    elif opcio == 4:
        cara_max = int(input("¿Cuántas caras tiene el dado?: "))
        num_tirades = int(input("¿Cuántos dados quieres lanzar?: "))
        resultats = daus_x(cara_max, num_tirades)
        print(f"Resultados de las tiradas: {resultats}")
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
