import random

# Ghiceste numarul
# Implementati acest joc simplu:

# Calculatorul alege un numar la intamplare, intre 1 si 100
# Utilizatorul are la dispozitie 7 incercari sa ghiceasca numarul
# Daca utilizatorul a ghicit numarul in una dintre incercari, jocul se termina, a castigat.
# Daca nu l-a ghicit si mai are incercari, calculatorul ii va da cate un indiciu sub forma unui mesaj: 'Numarul secret e mai mare' sau 'Numarul secret e mai mic'
# Daca nu l-a ghicit si nu mai are incercari, jocul s-a terminat, a pierdut.
# Nota: ar fi util sa afisati utilizatorului la fiecare pas cate incercari mai are (sau care e numarul incercarii curente)

numar_utilizator = int(input("Numarul ales de tine este: "))
random_number = random.randint(1, 100)
incercari = 7
print(random_number)


while random_number != numar_utilizator:
    if numar_utilizator < random_number:
        print("Numarul secret e mai mare.")
    else:
        print("Numarul secret e mai mic")
    incercari -= 1
    print(f"Mai ai {incercari} incercari")
    numar_utilizator = int(input("Numarul ales de tine este: "))
    if incercari == 1:
        break

if numar_utilizator == random_number:
    print("Felicitari! Ai ghicit numarul")

