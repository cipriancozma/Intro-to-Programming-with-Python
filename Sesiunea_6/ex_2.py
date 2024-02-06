# Cifrul lui Cezar (30+20p)
# a) Cifrare text (30p)
# Scrieti 2 functii care permit cifrarea si descifrarea unui text folosind cifrul lui Cezar - vezi detalii aici: Caesar cipher (wikipedia)

# functiile vor primi cate 2 parametrii:

# text - valoarea initiala pentru cifrat/descifrat (o valoare tip string)
# deplasament - valoarea deplasamentului de folosit (un numar intreg)
# functiile vor intoarce textul transformat (cifrat/ descrifrat), ca o valoare string.

# Note:

# este esential ca programul sa poata descifra corect un text cifrat cu acelasi program (si folosind acelasi deplasament):

# descifreaza(cifreaza('abcxyz',7),7) == 'abcxyz'

# este preferabil sa se foloseasca cifrarea Cezar 'standard', avand grija la cazurile de depasire a intervalului a..z:

# cifreaza('xyz',2) == 'zab' (NU 'z{|')

# descifreaza('zab',2) == 'xyz'

# este preferabil sa cifreze doar literele textului ('a'..'z','A'..'Z') lasand celelalte caractere (numere, simboluri) neschimbate:

# print(cifreaza('trimite intariri, 3 cohorte!', 13)) # afiseaza: 'gevzvgr vagnevev, 3 pbubegr!'

# Indiciu: amintiti-va despre codurile ASCII si despre functiile Python chr() si ord()

# Intrebare: avem nevoie de doua functii similare aici, care repeta cod intre ele, sau ne putem folosi de functia pentru cifrare si in cazul descrifrarii?

# Exemple:

# print(cifreaza('abcxyz 123?!', 3))  # afiseaza: 'defabc 123?!'
# print(descifreaza('defabc 123?!', 3))  # afiseaza: 'abcxyz 123?!'

# cifreaza_fisier('mesaj.txt', 5) # creaza mesaj.txt_encoded, cu continut cifrat
# descifreaza_fisier('mesaj.txt_encoded', 5) # creaza mesaj.txt_encoded_decoded, cu continut la fel cu cel initial
# b) Cifrare fisier [Optional,+20p]
# Scrieti 2 functii care permit cifrarea si descifrarea continutului unui fisier folosind cifrul lui Cezar:

# primesc 2 parametrii de intrare: numele fisierului initial (de cifrat/descifrat) si deplasamentul
# nu intorc nici o valoare
# citesc continutul fisierului dat, cifreaza/descifreaza fiecare linie si scriu rezultatul intr-un nou fisier, cu nume similar cu fisierul vechi dar cu sufixul '_cifrat'/'_descifrat' adaugat la final.
# Testati functia cu un fisier text, asigurandu-va ca poate cifra si descifra cu succes un fisier text existent, obtinand un fisier cu acelasi continut ca cel initial (cand se foloseste acelasi deplasament).

# Indiciu: va puteti folosi de functiile implementate la a)

def cifreaza(text, deplasament):
  text_nou = ''
  for litera in text:
    if 'a' <= litera <= 'z':
      litera_to_int = (ord(litera) - ord('a') + deplasament) % 26 + ord('a')
      text_nou += chr(litera_to_int)
    elif 'A' <= litera <= 'Z':
      litera_to_int = (ord(litera) - ord('A') + deplasament) % 26 + ord('A')
      text_nou += chr(litera_to_int)
    else:
      text_nou += litera
  return text_nou


# print(cifreaza('xyz', 2))
# print(cifreaza('trimite intariri, 3 cohorte!', 13)) # afiseaza: 'gevzvgr vagnevev, 3 pbubegr!'
# print(cifreaza('abcxyz 123?!', 3))  # afiseaza: 'defabc 123?!'

def descifreaza(text,deplasament):
  text_nou = ''
  for litera in text:
    if 'a' <= litera <= 'z':
      litera_to_int = (ord(litera) - ord('a') - deplasament) % 26 + ord('a')
      text_nou += chr(litera_to_int)
    elif 'A' <= litera <= 'Z':
      litera_to_int = (ord(litera) - ord('A') - deplasament) % 26 + ord('A')
      text_nou += chr(litera_to_int)
    else:
      text_nou += litera
  return text_nou

# print(descifreaza('zab', 2))

def cifru_cezar(text, deplasament, cifrare=True):
  text_nou = ''
  semn_deplasament = deplasament
  if not cifrare:
    semn_deplasament = -deplasament
  for litera in text:
    if 'a' <= litera <= 'z':
      litera_to_int = (ord(litera) - ord('a') + semn_deplasament) % 26 + ord('a')
      text_nou += chr(litera_to_int)
    elif 'A' <= litera <= 'Z':
      litera_to_int = (ord(litera) - ord('A') + semn_deplasament) % 26 + ord('A')
      text_nou += chr(litera_to_int)
    else:
      text_nou += litera
  return text_nou

# print(cifru_cezar('zab', 2, False))
# print(cifru_cezar('xyz', 2))


def cifrare_fisier(fisier, deplasament):
  if "." in fisier:
    nume_fisier, extensie = fisier.rsplit(".", 1)
    fisier_cifrat = f"{nume_fisier}_cifrat.{extensie}"
  else:
    fisier_cifrat = f"{fisier}_cifrat"
    
  with open(fisier, 'r') as fisier_orig, open(fisier_cifrat, 'w') as fisier_nou:
    for linie in fisier_orig:
      linie_striped = linie.strip()
      linie_cifrata = cifru_cezar(linie_striped, deplasament)
      fisier_nou.write(linie_cifrata + "\n")


# print(cifrare_fisier("./words.txt", 3))

def decifrare_fisier(fisier, deplasament):
  if "." in fisier:
    nume_fisier, extensie = fisier.rsplit(".", 1)
    fisier_decifrat = f"{nume_fisier}_decifrat.{extensie}"
  else:
    fisier_decifrat = f"{fisier}_decifrat"

  with open(fisier, 'r') as fisier_orig, open(fisier_decifrat, 'w') as fisier_nou:
    for linie in fisier_orig:
      linie_striped = linie.strip()
      linie_decifrata = cifru_cezar(linie_striped, deplasament, False)
      fisier_nou.write(linie_decifrata + "\n")

decifrare_fisier('./words_cifrat.txt', 3)