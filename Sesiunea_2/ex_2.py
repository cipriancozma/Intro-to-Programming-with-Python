# Semn (15p)
# Scrieti o functie semn(n) care implementeaza functia semn din matematica, definita astfel: o functie care primeste ca parametru un numar si returneaza ca rezultat una din valorile: -1 daca numarul e negativ, +1 daca e pozitiv sau 0 daca e egal cu zero.

# Exemple:

# print(semn(-3))  # afiseaza: -1
# print(semn(0))   # afiseaza:  0
# print(semn(7))   # afiseaza:  1

def semn(n):
  if n > 0:
    return 1
  elif n < 0:
    return -1
  else:
    return 0

print(semn(-3))
print(semn(0))
print(semn(7))