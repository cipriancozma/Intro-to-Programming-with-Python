# Note studenti (20p)
# Scrieti o functie analizeaza_note(lista_note) care primeste ca parametru o lista de numere reprezentand notele unei grupe de studenti (numere intregi, intre 1 si 10) si calculeaza si afiseaza nota minima, maxima si media lor aritmetica.

# Nota: pentru o eficienta mai buna, incercati sa folositi o singura bucla (daca nu reusiti, e acceptabil sa folositi si 2-3 bucle)

# Exemple:

# analizeaza_note([])            # afiseaza: Eroare: nu exista note de analizat
# analizeaza_note([8])           # afiseaza: Min: 8, max: 8, media: 8.0
# analizeaza_note([7, 8, 5, 9])  # afiseaza: Min: 5, max: 9, media: 7.25

def analizeaza_note(lista_note):
  if len(lista_note) == 0:
    print("Eroare: nu exista note de analizat")
    return

  minim = maxim = suma = lista_note[0]

  for note in lista_note[1:]:
    minim = min(minim, note)
    maxim = max(maxim, note)
    suma += note

  media = suma / len(lista_note)
  print(f"Min: {minim}, Max: {maxim}, media: {media}") 



analizeaza_note([])            # afiseaza: Eroare: nu exista note de analizat
analizeaza_note([8])           # afiseaza: Min: 8, max: 8, media: 8.0
analizeaza_note([7, 8, 5, 9])  # afiseaza: Min: 5, max: 9, media: 7.25
