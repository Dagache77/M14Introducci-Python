# Dades d'usuari i contrasenya
usuari_guardat = "usuari_exemple"
contrasenya_guardada = "contrasenya_exemple"

# Demana a l'usuari que introdueixi les credencials
usuari_input = input("Introdueix el teu usuari: ")
contrasenya_input = input("Introdueix la teva contrasenya: ")

# Verifica les credencials
if usuari_input == usuari_guardat and contrasenya_input == contrasenya_guardada:
    print("Benvingut al sistema, {}!".format(usuari_input))
else:
    print("Error d'autenticació. Les credencials no són vàlides.")
