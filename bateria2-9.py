nota = float(input("Introdueix la teva nota: "))

if 1 <= nota <= 4:
    print("Insuficient")
elif nota == 5:
    print("Suficient")
elif nota == 6:
    print("Bé")
elif 7 <= nota <= 8:
    print("Notable")
elif 9 <= nota <= 10:
    print("Excel·lent")
else:
    print("Nota no vàlida. La nota ha de ser entre 1 i 10.")
