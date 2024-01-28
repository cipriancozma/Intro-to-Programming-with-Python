# Actualizare lista (15p)
# Scrieti of functie multiplica(lista_numere, factor) care:

# primeste 2 parametrii, o lista de numere si un alt numar separat
# nu intoarce nici un rezultat
# face o actualizare directa a elementelor din lista data (nu intr-o copie ai ei) inmultind fiecare element cu numarul dat 'factor'
# Indiciu: va fi nevoie sa iterati lista folosind varianta de bucla cu index

# Exemple:

# numere = [2, 5, 1, 7]
# multiplica(numere, 3)  # actualizeaza lista, nu returneaza nimic
# print(numere)  # afiseaza: [6, 15, 3, 21]

def multiplica(lista_numere, factor):
  for idx in range(len(lista_numere)):
    lista_numere[idx] *= factor

numere = [2, 5, 1, 7]
multiplica(numere, 3)
print(numere)