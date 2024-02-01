#  [Optional] Bon casa (40p)
# Scrieti o functie afiseaza_bon( preturi_produse, numar_produse) care:

# primeste 2 parametrii de tip dictionar:

# preturi_produse - dictionar in care cheile sunt numele produselor si valorile sunt pretul pentru fiecare (pe bucata)
# numar_produse - dictionar in care cheile sunt numele produselor (aceleasi ca in primul) iar valorile sunt numarul de produse cumparate din fiecare tip
# nu intoarce nici un rezultat

# afiseaza un bon cu informatii despre produsele cumparate:

# pentru fiecare produs tipareste o line care include: numele produsului, pretul pe bucata, numarul de bucati cumparate si pretul total
# la sfarsit va include si o linie final cu numarul total de produse si pretul total pentru intreaga lista.
# Note:

# in mod normal dictinarele ar trebuie sa contina aceleasi nume de produse (acelasi set de chei); daca insa un nume de produs exista doar intr-unul din dictionare, aceasta e considerata o greseala, si acel produs ar trebui ignorat (sa nu fie inclus in bon)

# pentru o afisare clara, incercati sa afisati preturile rotunjite la doar doua cifre zecimale

# Exemplu:

# pentru acest cod:

# preturi_produse = {'banane': 0.99, 'lapte': 1.5, 'paine': 1.2, 'whisky': 4.9}
# numar_produse = {'lapte': 2, 'paine': 1, 'banane': 3, 'miere': 10}
# afiseaza_bon(preturi_produse, numar_produse)
# se va afisa:

# Produse cumparate:
#  - banane: 0.99 x 3 = 2.97
#  - lapte: 1.50 x 2 = 3.00
#  - paine: 1.20 x 1 = 1.20
# TOTAL: 6 produse = 7.17 ron

def afiseaza_bon(preturi_produse, numar_produse):
  print("Produse cumparate: ")
  count_produse = 0
  total_produse = 0
  for cheie, valoare in preturi_produse.items():
    if cheie in numar_produse:
      total = valoare * numar_produse[cheie]
      count_produse += numar_produse[cheie]
      total_produse += total
      print(f"-{cheie}: {valoare} x {numar_produse[cheie]} = {total:.2f}")
  print(f"TOTAL: {count_produse} produse = {total_produse} ron")


preturi_produse = {'banane': 0.99, 'lapte': 1.5, 'paine': 1.2, 'whisky': 4.9}
numar_produse = {'lapte': 2, 'paine': 1, 'banane': 3, 'miere': 10}
afiseaza_bon(preturi_produse, numar_produse)