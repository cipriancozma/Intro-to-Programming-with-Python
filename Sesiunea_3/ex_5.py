# a) Scrite o functie incepe_cu(text, litera) care verifica daca un text dat incepe cu o litera data, si returneaza un rezultat boolean (True daca incepe, False in caz contrar)

# Exemple:

# print(incepe_cu('bax', 'b'))  # afiseaza: True
# print(incepe_cu('bax', 'a'))  # afiseaza: False
# print(incepe_cu('', 'a'))  # afiseaza: False
# b) Scrieti o functie terminat_cu(text,litera) care verifica daca un text dat se termina cu o litera data, si returneaza un rezultat boolean (True daca incepe, False in caz contrar)

# Exemple:

# print(terminat_cu('bax', 'x'))  # afiseaza: True
# print(terminat_cu('bax', 'y'))  # afiseaza: False
# print(terminat_cu('', 'a'))  # afiseaza: False
# c) [Optional,+20p] Scrieti o functie afiseaza_cuvintele_cu(prima_litera,ultima_litera) care citeste toate cuvintele dintr-un fisier text ('words.txt', care contine cate un singur cuvant pe linie), le analizeaza si afiseaza doar cuvintele care incep si se termina cu cele 2 litere date.

# Indicii:

# puteti refolosi aici si functiile definite la punctele a),b)

# pentru a citi toate liniile dintr-un fisier text, puteti folosi o bucla 'for', vedeti detalii aici

# fisierul text 'words.txt' contine cate un cuvant pe fiecare linie, incluzand la final si terminatorul de linie '\n'; puteti elimina acest caracter special folosind functia predefinita strip() disponibila pe valorile tip string.

# d) [Optional,+10p] Completati functia de la c) astfel incat sa si numere cuvintele care indeplinesc conditia de afisare si sa afiseze numarul de cuvinte la final.

# Testati apoi functia de la c)/d) pentru cateva combinatii de litere.

# Exemple: afiseaza_cuvintele_cu('e', 'x') va afisa:

# Cuvintele care incep cu e si se termina in x:
# echinox
# eflux
# eterodox
# Numar cuvinte gasite: 3

def incepe_cu(text, litera):
  if text == '' or litera == '':
    return False
  return text[0] == litera

# print(incepe_cu('bax', 'b'))  # afiseaza: True
# print(incepe_cu('bax', 'a'))  # afiseaza: False
# print(incepe_cu('', 'a'))  # afiseaza: False

def terminat_cu(text, litera):
  if text == '' or litera == '':
    return False
  return text[len(text) - 1] == litera

# print(terminat_cu('bax', 'x'))  # afiseaza: True
# print(terminat_cu('bax', 'y'))  # afiseaza: False
# print(terminat_cu('', 'a'))  # afiseaza: False

def afiseaza_cuvintele_cu(prima_litera, ultima_litera):
  cuvinte_gasite = []
  with open('./words_ro.txt', 'r') as file:
    open_words = file.read().split()

    for cuvant in open_words:
      if cuvant.startswith(prima_litera) and cuvant.endswith(ultima_litera):
        cuvinte_gasite.append(cuvant)

  print(f"Cuvintele care incep cu {prima_litera} si se termina in {ultima_litera}: ")
  for cuvinte in cuvinte_gasite:
    print(cuvinte)

  print(f"Numar cuvinte gasite: {len(cuvinte_gasite)}")


print(afiseaza_cuvintele_cu('e', 'x'))
# print(afiseaza_cuvintele_cu('a', 'r'))
