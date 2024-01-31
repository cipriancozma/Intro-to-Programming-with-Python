# Inlocuire text (30p)
# Scrieti o functie inlocuieste(text, cuvinte_de_inlocuit) care primeste ca parametrii un text (o valoare string) si niste cuvinte de inlocuit (date sub forma unui dictionar in care fiecare cheie e un cuvant de inlocuit si valoarea e cuvantul nou), si returneaza un text nou in care cuvintele specificate au fost inlocuite.

# Indicii:

# pentru a inlocuit o parte dintr-un string (un substring) cu un nou string, puteti folosi functia predefinita replace() disponibila pentru valorile string, vezi mai multe detalii aici

# citeste in cartea 'Think Python' (cap 11) mai multe despre modalitatea mai compacta de a itera in acelasi timp si peste cheile si peste valorile unui dictionar, ca si perechi: for cheie,valoare in dictionar.items():

# Exemple:

# print(inlocuieste('Ana are mere', {'mere': 'cirese', 'Ana': 'Ion'}))  # afiseaza: Ion are cirese
# print(inlocuieste('aa bb cc aa dd ee', {'aa': 'A', 'dd': ''}))  # afiseaza: A bb cc A  ee

def inlocuieste(text, cuvinte_de_inlocuit):
  for cheie, valoare in cuvinte_de_inlocuit.items():
    text = text.replace(cheie, valoare)
  return text
      

print(inlocuieste('Ana are mere', {'mere': 'cirese', 'Ana': 'Ion'}))  # afiseaza: Ion are cirese
print(inlocuieste('aa bb cc aa dd ee', {'aa': 'A', 'dd': ''}))  # afiseaza: A bb cc A  ee