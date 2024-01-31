# Elemente distincte (25p)
# Scrieti o functie distincte(lista) care primeste ca parametru o lista de elemente (pot fi numere, stringuri) si returneaza o lista noua care contine doar elementele distincte din lista (fara duplicate), in aceeasi ordine ca in lista initiala.

# Nota: aceasta ar trebuie sa fie o lista nou construita, iar lista initiala sa ramana neschimbata.

# Indiciu: puteti itera peste lista veche si adauga elementele in noua lista, dar doar atunci cand ele nu sunt deja in noua lista...

# Exemple:

# numere = [3, 5, 2, 5, 3, 7]
# print(distincte(numere))  # afiseaza: [3, 5, 2, 7]
# print(numere)  # afiseaza: [3, 5, 2, 5, 3, 7] (nemodificata)

# print(distincte(['aa', 'bb', 'aa', 'cc'])) # afiseaza: ['aa', 'bb', 'cc']

def distincte(lista):
  lista_noua = []

  for item in lista:
    if item not in lista_noua:
      lista_noua.append(item)

  return lista_noua


numere = [3, 5, 2, 5, 3, 7]
print(distincte(numere))  # afiseaza: [3, 5, 2, 7]
print(numere)  # afiseaza: [3, 5, 2, 5, 3, 7] (nemodificata)

print(distincte(['aa', 'bb', 'aa', 'cc'])) # afiseaza: ['aa', 'bb', 'cc']