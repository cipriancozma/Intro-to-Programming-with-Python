# Capete text (20p)
# a) Scrieti o functie capete(text) care primeste ca parametru un text si returneaza o valoare string prescurtata care contine doar prima si ultima litera a textului initial.

# Observatie: asigurati-va ca tratati corect cazurile limita:

# cuvant gol ('') -> returneaza tot cuvant gol (NU eroare)
# cuvane doar de o litera (ex: 'a') -> returneaza cuvantul original (NU 'aa' sau eroare)
# Intrebare: puteti acoperi aceste doua cazuri impreuna, adaugand un singur 'if' in cod? (fara ramuri 'elif'/'else')

# Exemple:

# print(capete(''))  # afiseaza: ''
# print(capete('a'))  # afiseaza: 'a'
# print(capete('ab'))  # afiseaza: 'ab'
# print(capete('abcd'))  # afiseaza: 'ad'
# b) Scrieti o functie fara_capete(text) care primeste ca parametru un text si returneaza o valoare string similara cu textul initial, dar fara prima si ultima litera.

# Observatie: asigurati-va ca tratati corect cazurile in care cuvantul initial are mai putin de 3 litere.

# Exemple:

# print(fara_capete(''))  # afiseaza: ''
# print(fara_capete('a'))  # afiseaza: ''
# print(fara_capete('ab'))  # afiseaza: ''
# print(fara_capete('abc'))  # afiseaza: 'b'
# print(fara_capete('abcd'))  # afiseaza: 'bc'

def capete(text):
  if len(text) <= 1:
    return text
  else:
    return f"{text[0]}{text[len(text)-1]}"

# print(capete(''))  # afiseaza: ''
# print(capete('a'))  # afiseaza: 'a'
# print(capete('ab'))  # afiseaza: 'ab'
# print(capete('abcd'))  # afiseaza: 'ad'


def fara_capete(text):
  if len(text) < 3:
    return ''
  else:
    return text[1:-1]

# print(fara_capete(''))  # afiseaza: ''
# print(fara_capete('a'))  # afiseaza: ''
# print(fara_capete('ab'))  # afiseaza: ''
# print(fara_capete('abc'))  # afiseaza: 'b'
# print(fara_capete('abcd'))  # afiseaza: 'bc'
