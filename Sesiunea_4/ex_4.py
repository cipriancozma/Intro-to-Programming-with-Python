# Cuvinte alfabetice (20+20p)
# Spunem ca un cuvant este 'alfabetic' daca literele lui sunt deja ordonate in ordine alfabetica.

# a) Scrieti o functie e_alfabetic(cuvant) care primeste ca parametru un cuvant (o valoare string) si returneaza o valoare tip boolean: True daca cuvantul e alfabetic, False in caz contrar.

# Indiciu: se poate rezolva in mai multe moduri:

# iterati peste literele cuvantului (cu o bucla cu index) si verificati daca fiecare pereche de litere succesive e in ordinea corecta (pozitia i vs i+1..)

# SAU: convertiti cuvantul la o lista de caractere (vedeti exemplul de cod din clasa, cu folosirea functiei list()), apoi sortati acea lista de caractere o transformati inapoi intr-o valoare string, si apoi o puteti compara cu cuvantul initial...

# Exemple:

# print(e_alfabetic('aefgz'))  # afiseaza: True
# print(e_alfabetic('aefgc'))  # afiseaza: False
# b) [OPTIONAL,+20p]: Scrieti alta functie cuvinte_alfabetice_din_fisier() care citeste toate cuvintele dintr-un fisier text 'words.txt' si tipareste din doar cuvintele care sunt alfabetice, incluzand de asemenea si numarul lor la final (indiciu: puteti folosi functia de la a) pentru filtrarea cuvintelor)

# Exemple: cuvinte_alfabetice_din_fisier() afiseaza:

# Cuvintele alfabetice din fisier:
# abc
# abces
# abil
# abis
# …
# prr
# pst
# sst
# Total cuvinte gasite: 209

def e_alfabetic(cuvant):
  cuvant_original = cuvant
  cuvant_list = list(cuvant)
  cuvant_list.sort()
  cuvant_nou = ''.join(cuvant_list)
  return cuvant_original == cuvant_nou


# print(e_alfabetic('aefgz'))  # afiseaza: True
# print(e_alfabetic('aefgc'))  # afiseaza: False


def cuvinte_alfabetice_din_fisier():
  numar_cuvinte = 0
  print("Cuvintele alfabetice din fisier: ")
  with open('./words_ro.txt', 'r') as fisier:
    for linie in fisier:
      cuvant = linie.strip()
      if e_alfabetic(cuvant):
        print(cuvant)
        numar_cuvinte += 1

  print(f"Total cuvinte gasite: {numar_cuvinte}")


cuvinte_alfabetice_din_fisier()
