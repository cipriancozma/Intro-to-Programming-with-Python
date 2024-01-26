# a) Scrieti o metoda contine(text,litera) care primeste ca parametrii un text si o litera, si returneaza valoarea boolean True daca textul contine acea litera, sau False in caz contrar.

# Observatie: nu aveti voie sa folosit operatorul predefinit in direct (ca de exemplu: return litera in text), ci ar trebui sa folositi iteratii manuale (bucle while/for)
# b) Scrieti o metoda aparitii(text, litera) care numara de cate ori apare litera data in textul dat, si returneaza acest numar.

# Observatie: nu aveti voie sa folositi functia predefinita count (ca de exemplu: return text.count(litera))
# c) Scrieti o metoda numar_vocale(text) care numara cate vocale contine textul dat (una din literele 'a','e','i','o', 'u', incluzand aparitiile multiple)

# Optional: incercati sa numerati corect atat literele mici cat si cele mari ('a' si 'A'...), folosind metodele upper()/lower() de pe string.
# Exemple:

# print(contine('abcde', 'b'))  # afiseaza: True
# print(contine('abbbe', 'b'))  # afiseaza: True
# print(contine('abcde', 'x'))  # afiseaza: False
# print(contine('', 'x'))  # afiseaza: False

# print(aparitii('aabcdeef', 'e'))  # afiseaza: 2
# print(aparitii('aabcdeef', 'y'))  # afiseaza: 0
# print(aparitii('', 'y'))  # afiseaza: 0

# print(numar_vocale('a fost odata un emir..'))  # afiseaza: 8

def contine(text, litera):
  for lit in text:
    if lit == litera:
      return True
  return False

# print(contine('abcde', 'b'))  # afiseaza: True
# print(contine('abbbe', 'b'))  # afiseaza: True
# print(contine('abcde', 'x'))  # afiseaza: False
# print(contine('', 'x'))  # afiseaza: False

def aparitii(text, litera):
  count = 0
  for lit in text:
    if lit == litera:
      count += 1
  return count

# print(aparitii('aabcdeef', 'e'))  # afiseaza: 2
# print(aparitii('aabcdeef', 'y'))  # afiseaza: 0
# print(aparitii('', 'y'))  # afiseaza: 0

def numar_vocale(text):
  text_lowercase = text.lower()
  vocale = ['a', 'e', 'i', 'o', 'u']
  count = 0
  for litera in text_lowercase:
    if litera in vocale:
      count += 1
  return count

# print(numar_vocale('a fost odata un emir..'))  # afiseaza: 8