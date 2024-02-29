# Pregunta quantes vides té l'usuari
vides = int(input("Quantas vides tens? "))

# Mostra les vides inicials
print("Vides inicials:", vides)

# Bucle principal
while vides > 0:
    accio = input("Prem 'k' per perdre una vida (o 'q' per sortir): ")

    # Verifica la tecla premuda
    if accio == 'k':
        vides -= 1  # Es perd una vida
        print("Has perdut una vida. Vides restants:", vides)
    elif accio == 'q':
        print("Has sortit del joc.")
        break  # Sortir del bucle si es prem 'q'
    else:
        print("Tecla no vàlida. Prem 'k' o 'q'.")

# Comprova si s'han exhaurit les vides
if vides == 0:
    print("Game Over")
