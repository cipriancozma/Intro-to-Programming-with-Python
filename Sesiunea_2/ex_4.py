# Cifra comuna (15p)
# Scrieti o functie numita cifra_comuna(x,y) care primeste ca parametrii 2 numere intregi si returneaza valoarea boolean True doar in cazul in care ambele numere au exact 2 cifre (sunt in intervalul 10..99) si au macar o cifra comuna, altfel returneaza valoarea False.

# Exemple:

# print(cifra_comuna( 3, 33))   # afiseaza: False
# print(cifra_comuna( 34, 28))  # afiseaza: False
# print(cifra_comuna( 34, 48))  # afiseaza: True
# print(cifra_comuna( 34, 33))  # afiseaza: True
# print(cifra_comuna( 34, 43))  # afiseaza: True
# Indiciu: puteti folosi operatorii // si % pentru extragerea cifrelor individuale

def cifra_comuna(x, y):
  str_x = str(x)
  str_y = str(y)

  if len(str_x) == len(str_y):
    for item in str_x:
      if item in str_y:
        return True
  return False


print(cifra_comuna(3, 33))
print(cifra_comuna(34, 28))
print(cifra_comuna(34, 48))
print(cifra_comuna(34, 33))
print(cifra_comuna(34, 43))
