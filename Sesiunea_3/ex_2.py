# Prima putere peste (20p)
# Scrieti o functie numita prima_putere_peste(baza, limita) care primeste ca parametrii 2 numere (amble numere intregi pozitive), apoi calculeaza puterile succesive ale numarului baza, incepand de la 1 (=baza la puterea 0) si oprindu-se la prima putere care este mai mare decat valoarea limita data, si returnaza ca rezulat final valoarea acelei puteri (cea imediat peste limita).

# Indiciu: in scopul urmaririi mai usoare a logicii codului, functia poate afisa diferite valori (puterile intemediare, valoarea finala), dar partea importanta e sa faca return valorii corecte la final.
# Exemple:

# print(prima_putere_peste(3, 0))  # afiseaza: 1
# print(prima_putere_peste(2, 1020))  # afiseaza: 1024
# print(prima_putere_peste(2, 1025))  # afiseaza: 2048
# print(prima_putere_peste(7, 10000))  # afiseaza: 16807

def prima_putere_peste(baza, limita):
  putere = 0
  valoare_curenta = 1

  while valoare_curenta <= limita:
    putere += 1
    valoare_curenta = baza ** putere
    print(valoare_curenta)
  
  return valoare_curenta

# print(prima_putere_peste(3, 0))
print(prima_putere_peste(2, 1020))
# print(prima_putere_peste(2, 1025))
# print(prima_putere_peste(7, 10000))