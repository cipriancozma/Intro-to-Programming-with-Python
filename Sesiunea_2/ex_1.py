# Verificare paritate (10p)
# Scrieti o functie par_impar(n) care primeste ca parametru un numar intreg si returneaza un rezultat de tip string, care contine una dintre valorile 'par'/'impar', in functie de paritatea numarului.

# Exemple:

# print(par_impar(6))  # afiseaza: 'par'
# print(par_impar(3))  # afiseaza: 'impar'


def par_impar(n):
  if n % 2 == 0:
    return "par"
  else:
    return 'impar'

print(par_impar(6))
print(par_impar(3))