# Scrieti o functie paranteze_corecte(expresie) care primeste ca parametru o expresie (o valoare string) care poate contine paranteze rotunde si diverse alte caractere, si verifica daca parantezele sunt toate corect deschise si inchise.

# Regulile generale pentru a fi corecte:

# toate parantezele trebuie sa aiba pereche (ar trebui sa avem acelasi numar de paranteze deschise si inchise)
# fiecare pereche de paranteze trebuie sa inceapa cu cea deschisa (nu poate sa inceapa cu cea inchisa)
# Functia ar trebui sa intoarca un rezultat de tip boolean: True daca expresia e corecta, False in caz contrar.

# Exemple:

# print(paranteze_corecte(''))                  # afiseaza: True
# print(paranteze_corecte('abc 12'))            # afiseaza: True
# print(paranteze_corecte('abc ()'))            # afiseaza: True
# print(paranteze_corecte('x*(y+z), (2+3)'))    # afiseaza: True
# print(paranteze_corecte('(1+(2+3))-4'))       # afiseaza: True
# print(paranteze_corecte('(.()..((?))..)..'))  # afiseaza: True

# print(paranteze_corecte('(..'))         # afiseaza: False
# print(paranteze_corecte('..)(..()..'))  # afiseaza: False
# print(paranteze_corecte('..()..)'))     # afiseaza: False
# Indiciu: se poate rezolva cu o singura bucla: iterati peste expresie si definiti 2 variabile contor, una care numara parantezele inchise si una pentru cele deschise; apoi ganditi-ta care sunt cazurile in care expresia este invalida, pe baza modului in care aceste 2 valori evolueaza, pana la sfarsitul expresiei..._

def paranteze_corecte(expresie):
  count_paranteze_deschise = 0
  count_paranteze_inchise = 0

  for char in expresie:
    if char == '(':
      count_paranteze_deschise += 1
    elif char == ')':
      count_paranteze_inchise += 1

    if count_paranteze_inchise > count_paranteze_deschise:
      return False
  return count_paranteze_deschise == count_paranteze_inchise
  

print(paranteze_corecte(''))                  # afiseaza: True
print(paranteze_corecte('abc 12'))            # afiseaza: True
print(paranteze_corecte('abc ()'))            # afiseaza: True
print(paranteze_corecte('x*(y+z), (2+3)'))    # afiseaza: True
print(paranteze_corecte('(1+(2+3))-4'))       # afiseaza: True
print(paranteze_corecte('(.()..((?))..)..'))  # afiseaza: True

print(paranteze_corecte('(..'))         # afiseaza: False
print(paranteze_corecte('..)(..()..'))  # afiseaza: False
print(paranteze_corecte('..()..)'))     # afiseaza: False