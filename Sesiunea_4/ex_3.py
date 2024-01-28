# Gasire duplicate (15p)
# Scrieti o functie gasire_duplicate(lista_cuvinte) care primeste ca parametru o lista de cuvinte (valori tip string), verifica daca sunt valori duplicate intre ele si afiseaza o concluzie la final (cuprinde sau nu duplicate, eventual care e primul duplicat gasit). Nu trebuie sa returneze nici o valoare.

# Nota: incercati sa va faceti codul cat mai rapid si eficient posibil, adica sa minimizati numarul de operatii efectuate (de exemplu, daca primeste o lista cu 100 cuvinte si pe pozitiile 1 si 3 e o pereche de duplicate, cate operatii, gen comparatii de stringuri, va face algoritmul pana se opreste?)

# Indiciu: iesirea 'rapida' din functii: daca intr-o functie aveti niste cod in interioriul unei bucle (posibil chiar intr-un sistem de mai multe bucle imbricate) si aveti nevoie sa iesiti deodata din toate buclele si de asemenea sa iesiti din functie direct, se poate folosi instructiunea return (fara nici o valoare dupa ea, daca functia nu are nevoie sa returneze vre-un rezultat la final); acest return va termina functia imediat.
# Exemple:

# gasire_duplicate(['aa', 'bb', 'cc', 'aa'])  # afiseaza: Am gasit o valoare duplicata: aa (pe pozitiile: 0, 3)
# gasire_duplicate(['aa', 'bb', 'cc', 'dd'])  # afiseaza: Nu contine nici o valoare duplicata

def gasire_duplicate(lista_cuvinte):
  for i in range(len(lista_cuvinte)):
    for j in range(i+1, len(lista_cuvinte)):
      print(i, j)
      if lista_cuvinte[i] == lista_cuvinte[j]:
        print(f"Am gasit o valoare duplicata: {lista_cuvinte[i]} pe pozitile: {i}, {j} ")
        return  
  print("Nu contine nici o valoare duplicata")

gasire_duplicate(
    ['aa', 'bb', 'cc',
     'aa'])  # afiseaza: Am gasit o valoare duplicata: aa (pe pozitiile: 0, 3)
gasire_duplicate(['aa', 'bb', 'cc',
                  'dd'])  # afiseaza: Nu contine nici o valoare duplicata