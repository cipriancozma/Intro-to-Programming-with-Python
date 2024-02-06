# Anagrame [Optional,+40p]
# a) Scrieti o a functie anagrame(cuvant1, cuvant2) care:

# primeste 2 parametrii de tip string
# verifica daca cele 2 valori sunt anagrame - adica daca contin exact acelasi set de litere (incluzand numarul de repetitii pentru fiecare), dar posibil in alta ordine
# intoarce un rezultat boolean (True daca sunt anagrame, False in caz contrar)
# Exemple:

# print(anagrame('intrau', 'ruinat'))  # afiseaza: True
# print(anagrame('baac', 'cabb'))  # afiseaza: False
# Indiciu: sunt posibile mai multe solutii:

# Puteti itera peste literele din fiecare cuvant, si sa numarati pentru fiecare din ele de cate ori apare (manual, sau folosind metoda string.count()), verificand apoi ca aveti acelasi set de perechi (litere+aparitii) pentru ambele cuvinte

# Alta solutie: e suficient sa sortati literele ambelor cuvinte, si apoi sa verificati daca aceste liste de litere sunt identice pentru cele 2 cuvinte (au aceleasi elemente in aceeasi ordine); pentru asta trebuie sa convertiti valorile string la liste de caractere, si sa le sortati (cu list.sort() sau sorted())...

# b): Scrieti o functie anagrame_pentru(cuvant) care:

# primeste ca parametru un cuvant initial (valoare string)
# citeste toate cuvintele dintr-un fisier text (words.txt) si cauta cuvintele care sunt anagrame pentru cuvantul dat (folosind functia de la primul punct)
# colecteaza aceste cuvinte anagram intr-o lista noua, eventual o sorteaza alfabetic si o intoarce ca si rezultat al functiei
# Nota: e preferabil sa excludeti cuvantul initial din lista lui de anagrame (daca apare si el in fisier)

# Exemple:

# print(anagrame_pentru('intrau'))  # afiseaza: ['natriu', 'nutria', 'ruinat', 'rutina', 'taurin', 'unitar', 'uranit']
# print(anagrame_pentru('barzi'))  # afiseaza: ['bariz', 'bizar']
# print(anagrame_pentru('altitudine'))  # afiseaza: ['latitudine']

# print(anagrame_pentru('acasa'))  # afiseaza: []
# print(anagrame_pentru('programator'))  # afiseaza: []

def anagrame(cuvant1, cuvant2):
  cuvant_1 = list(cuvant1)
  cuvant_2 = list(cuvant2)
  cuvant_1.sort()
  cuvant_2.sort()
  sorted_cuvant1 = " ".join(cuvant_1)
  sorted_cuvant2 = " ".join(cuvant_2)
  if sorted_cuvant1 == sorted_cuvant2:
    return True
  return False


# print(anagrame('intrau', 'ruinat'))  # afiseaza: True
# print(anagrame('baac', 'cabb'))  # afiseaza: False


def anagrame_pentru(cuvant):
  with open("./words.txt") as fisier:
    array_nou = []
    for linie in fisier:
      linie_striped = linie.strip()
      if cuvant == linie_striped:
        continue
      if anagrame(cuvant, linie_striped):
        array_nou.append(linie_striped)
    return array_nou


print(anagrame_pentru('intrau'))  # afiseaza: ['natriu', 'nutria', 'ruinat', 'rutina', 'taurin', 'unitar', 'uranit']
print(anagrame_pentru('barzi'))  # afiseaza: ['bariz', 'bizar']
print(anagrame_pentru('altitudine'))  # afiseaza: ['latitudine']

print(anagrame_pentru('acasa'))  # afiseaza: []
print(anagrame_pentru('programator'))  # afiseaza: []