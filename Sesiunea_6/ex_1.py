# Ordine jucatori (20p)
# Un grup de prieteni vor sa joace un joc, si trebuie sa decida ordinea in care vor incepe.

# Scrieti o functie care primeste o lista de nume (o singura valoare tip string, care cuprinde cateva nume separate de cate un spatiu), o transforma intr-o lista de valori string, alege o ordine aleatoarie pentru ele, le combina din nou intr-o singura linie (separate de spatii) si intoarce aceasta line (ca valoare tip string).

# Optional: cititi de la utilizator linia cu lista de nume si apoi afisati noua ordinea de start, folosindu-va si de functia de mai sus.

# Exemplu:

# # linie_nume = input('Introduceti lista de nume: ')
# linie_nume = 'Adi Bogdan Cristi Dana Elena Florin'
# print(amestecate(linie_nume))  # random, ex: 'Elena Bogdan Dana Florin Adi Cristi'

import random

linie_nume = input("Introduceti lista de nume: ")
def amestecate(linie_nume):
  nume_arr = linie_nume.split()
  random.shuffle(nume_arr)
  return " ".join(nume_arr)


print(amestecate(linie_nume))
