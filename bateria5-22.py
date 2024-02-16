# Fes un programa que guarda paraules introduïdes per l'usuari en un array i pregunta una paraula a l'usuari, el programa diu quantes vegades estava la paraula a la llista i l'elimina de la llista, per últim mostra la llista actualitzada.
paraules = []

while True:
    paraula = input("Introdueix una paraula (o 'final' per acabar): ")

    if paraula.lower() == "final":
        break

    paraules.append(paraula)

print("Llista de paraules inicial:", paraules)

paraula_a_buscar = input("Introdueix una paraula per buscar i eliminar: ")

vegades_trobada = paraules.count(paraula_a_buscar)
paraules = [paraula for paraula in paraules if paraula != paraula_a_buscar]

print(f"La paraula '{paraula_a_buscar}' estava {vegades_trobada} vegades a la llista.")
print("Llista actualitzada:", paraules)
