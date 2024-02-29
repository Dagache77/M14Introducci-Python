posicio_asterisc = 0  # Inicialitza la posició de l'asterisc a la primera posició.
AMPLADA = 20          # Longitud de la cadena d'asteriscs.

while True:   # Bucle infinit perquè el programa s'executi contínuament.

    # Genera una cadena de text amb l'asterisc a la seva posició actual.
    cadena_asterisc = ""
    for i in range(AMPLADA+1):
        if posicio_asterisc == i:
            cadena_asterisc += "*"
        else:
            cadena_asterisc += " "
    # Imprimeix la cadena d'asteriscs a la consola.
    print(cadena_asterisc)

    # Sol·licita a l'usuari que introdueixi un moviment ('a' o 'd').
    moviment = input("")

    #aplico el moviment de l'usuari:
    if moviment == 'a' and posicio_asterisc > 0:
            posicio_asterisc -= 1  # Mou l'asterisc cap a l'esquerra.
    elif moviment == 'd' and posicio_asterisc < AMPLADA:
            posicio_asterisc += 1  # Mou l'asterisc cap a la dreta.

