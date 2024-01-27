# Forma mai mare (20p: a/b=10)
# a) Scrieti o functie numita forma_mai_mare(raza,latura) care primeste ca parametrii 2 numere (posibil cu virgula) care reprezinta raza unui cerc si lungimea laturii unui patrat, calculeaza ariile celor 2 forme si returneaza o valoare de tip string, una din variantele 'cerc' sau 'patrat', in functie de care forma avea aria mai mare.

# Exemple:

# print(forma_mai_mare(10,5))   # afiseaza: 'cerc'  (aria: 314.15 vs 25)
# print(forma_mai_mare(10,20))  # afiseaza: 'patrat'  (aria: 314.15 vs 400)
# b) Optional: scrieti o a doua versiune a metodei de mai sus, numita forma_clar_mai_mare, cu aceasta diferenta: daca ariile celor doua forme sunt foarte apropiate ca valoare, adica daca diferenta lor (pozitiva sau negativa) e mai putin decat 1% din aria cercului, atunci va intoarce valoarea 'egale', altfel va intoarce 'cerc'/'patrat' dupa logica anterioara.

# Exemple:

# print(forma_clar_mai_mare(10,5))    # afiseaza: 'cerc'
# print(forma_clar_mai_mare(10,20))   # afiseaza: 'patrat'
# print(forma_clar_mai_mare(10,17.7)) # afiseaza: 'egale'   (aria: 314.15 vs 313.29)
# Indiciu: pentru a calcula modulul unui numar (a-i elimina semnul daca era negativ) puteti folosi functia abs, ex: abs(-3)

def forma_mai_mare(raza, latura):
  PI = 3.14
  aria_cerc = PI * raza**2
  aria_patrat = latura**2

  if aria_cerc > aria_patrat:
    return 'cerc'
  else:
    return 'patrat'

# print(forma_mai_mare(10,5))
# print(forma_mai_mare(10,20))

def forma_clar_mai_mare(raza, latura):
  PI = 3.14
  aria_cerc = PI * raza**2
  aria_patrat = latura**2

  apropiate_ca_valoare = abs(aria_cerc - aria_patrat) < 0.01 * aria_cerc
  if apropiate_ca_valoare:
    return "egale"
  elif aria_cerc > aria_patrat:
    return 'cerc'
  else:
    return 'patrat'
  
print(forma_mai_mare(10,5))
print(forma_mai_mare(10,20))
print(forma_clar_mai_mare(10,17.7))