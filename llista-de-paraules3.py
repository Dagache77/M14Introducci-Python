paraules = []

while 'final' not in paraules:
    paraules.append(input("Introdueix una paraula: "))

concatenacio = ' '.join(paraules[:-1])
print(f"La concatenació de les paraules és: {concatenacio}")
