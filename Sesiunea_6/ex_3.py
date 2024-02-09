# Joc spanzuratoarea (50+10p)
# a) Jocul de baza (50p)
# Implementati jocul de cuvinte 'spanzuratoarea':

# programul citeste o lista de cuvinte dintr-un fisier text (words.txt, contine cate un cuvant pe linie) si alege unul la intamplare

# afiseaza apoi cuvantul in forma lui 'mascata', in care fiecare litera e inlocuita cu caracterul '_', in afara de prima si ultima litera, considerate 'descoperite' de la inceput, ca indiciu

# nota: orice alta aparitie a celor doua litere in interiorul cuvantului va fi si ea 'demascata', de exemplu pentru cuvantul 'transportor' se va afisa la inceput 'tr_____rt_r'
# jucatorul are la dispozitie un numar maxim de incercari (ca de exemplu 7) in care trebuie sa ghiceasca toate literele cuvantului, pentru a castiga jocul

# bucla jocului: programul va cere jucatorului in mod repetat sa introduca cate o litera:

# daca litera introdusa e una din literele inca mascate din cuvant, atunci va fi demascata (in toate locurile in care apare in cuvant, daca sunt mai multe), iar numarul de incercari ramase ramane acelasi (nu scade)
# daca litera nu apartine deloc cuvantului, utilizatorul pierde una din incercari
# sfarsitul jocului:

# daca jucatorul a ghicit toate literele, a castigat
# daca a epuizat incercarile fara sa ghiceasca toate literele, a pierdut
# Indiciu: incercati sa va separati codul in mai multe functii mai mici, fiecare rezolvand doar cate o parte mai mica si clar delimitata a problemei - de exemplu o functie pentru alegerea unui cuvant aleator din fisier, una pentru obtinerea formei mascata a cuvantului, una pentru citirea unei litere inca neincercata inca de la jucator, etc. Iar in programul final trebuie doar sa le combinati intr-un mod potrivit (obtinand un cod doar de 20-30 linii, mai usor de citit)

import random

def replace_char(str, guessed_chars):
  first_letter = str[0]
  last_letter = str[-1]
  word = first_letter

  for char in str[1:-1]:
    if char in guessed_chars or char == first_letter or char == last_letter:
      word += char
    else:
      word += " _ "
  word += last_letter
  return word

with open('./words.txt') as file:
  words = file.readlines()
words = [word.strip() for word in words]
word = random.choice(words)
guessed_chars = []

tries = 7
if word:
  masked_word = replace_char(word, guessed_chars)
print("Cuvantul ales este: ", masked_word)

while tries > 0 and " _ " in masked_word:
  char = input("Introduceti litera: ")
  if char in word:
    if char not in guessed_chars:
      guessed_chars.append(char)
      print("Litera corecta!")
    else:
      print("Ai mai ghicit litera asta.")
  else:
    tries -= 1
    print(f"Ai gresit! Mai ai {tries} incercari")

  masked_word = replace_char(word, guessed_chars)
  print(f"Cuvantul ales este: {masked_word}")

  if " _ " not in masked_word:
    print(f"Ai ghicit cuvantul: {word}")
    break

if tries == 0:
  print(f"Nu mai ai incercari. Cuvantul era: {word}")
    