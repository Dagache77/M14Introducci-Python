limit_superior = int(input("Introdueix un límit superior: "))

print(f"Números primers fins a {limit_superior}:")
for num in range(2, limit_superior + 1):
    es_primer = True
    if num >= 2:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primer = False
                break
        if es_primer:
            print(num)
