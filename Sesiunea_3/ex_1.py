# ### Citire numar valid

# Scrieti o metoda citeste_intreg_pozitiv() care incearca sa citeasca un numar de la utilizator si continua sa ii ceara o valoare pana cand valoarea introdusa poate fi convertita cu success intr-un numar intreg pozitiv (adica e un string care contine doar caracterele '0'..'9', fara alte litere/simboluri) si apoi returneaza acel numar ca o valoare de tip int.

# Important: la introducerea unei valorile incorecte (ex: '12ab') programul nu trebuie sa se termine cu eroare, ci sa ceara o noua valoare corecta.

# Exemple:

# print('Numarul final citit:', citeste_intreg_pozitiv())
# results in this user interaction:

# >>> Introduceti un numar intreg pozitiv:
# abc
# >>> Introduceti un numar intreg pozitiv:
# 2.3
# >>> Introduceti un numar intreg pozitiv:
# -2
# >>> Introduceti un numar intreg pozitiv:
# 24
# >>> Numarul final citit: 24

def citeste_intreg_pozitiv(): 
  numar = input("Introduceti un numar intreg pozitiv: ")

  while not numar.isdigit():
    numar = input("Introduceti un numar intreg pozitiv: ")

  return int(numar)
  
print("Numarul final citit: ", citeste_intreg_pozitiv())