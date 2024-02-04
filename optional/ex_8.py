#  Eliminare duplicate
# Fiind data o lista de stringuri, eliminati din ea toate valorile duplicat. Valorile ramase trebuie sa ramana in aceeasi ordine ca in lista initiala.

# Observatie: functia trebuie sa modifice chiar lista initiala, nu sa intoarca o copie noua a ei.

# Exemple:

# cuvinte = ["a", "fost", "a", "a", "odata", "fost"]
# elimina_duplicate(cuvinte)
# print(f"dupa eliminare duplicate: {cuvinte}")



cuvinte = ["a", "fost", "a", "a", "odata", "fost"]

def elimina_duplicate(cuvinte):
    vazut = set()
    cuvinte[:] = [x for x in cuvinte if x not in vazut and not vazut.add(x)]

elimina_duplicate(cuvinte)
print(f"dupa eliminare duplicate: {cuvinte}")