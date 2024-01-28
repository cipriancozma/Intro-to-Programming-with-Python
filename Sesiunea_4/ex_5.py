# Cel mai lung cuvant (30+20p)
# a) Scrieti o functie cel_mai_lung(lista_cuvinte) care:

# primeste ca parametru o lista de cuvinte (o lista de valori tip string)
# analizeaza lista si gaseste cuvantul cel mai lung
# returneaza un rezultat de tip string: cel mai lung cuvant gasit, sau sirul gol ('') daca nu poate gasi cuvantul de lungime maxima (ex: lista goala)
# Exemple:

# cuvant = cel_mai_lung(['A', 'fost', 'odata', 'ca', 'niciodata', 'o', 'rata'])
# print(f'Cel mai lung: {cuvant}')  # afiseaza: Cel mai lung: niciodata

# cuvant = cel_mai_lung([])  # empty list
# print(f'Cel mai lung: {cuvant}')  # afiseaza: Cel mai lung:
# b) Scrieti o functie cel_mai_lung_din_fisier() care:

# nu primeste parametrii
# citeste toate cuvintele dintr-un fisier text (words.txt) si gaseste cel mai lung cuvant (unul dintre ele, daca sunt mai multe)
# returneaza acest cuvant (ca o valoare string)
# Indiciu: logica e similara cu functia de la a), dar nu veti putea refolosi direct acea functie, pentru ca asteapta ca parametru o lista de cuvinte, iar aici citim dintr-un fisier. Se poate rezolva asta citind mai intai din fisier si construind o lista cu toate cuvintle, apoi chemand prima functie. O varianta mai simpla ar putea fi insa doar sa copiati codul de la a) si sa faceti modificarile pentru a citi direct din fisier (nu dintr-o lista).

# Exemple:

# cuvant = cel_mai_lung_din_fisier()
# print(f'Cel mai lung din fisier: {cuvant} ({len(cuvant)} litere)')
# # afiseaza: Cel mai lung din fisier: electroencefalografie (21 litere)
# c) [OPTIONAL,+20p]: Scrieti o functie similara cele_mai_lungi_din_fisier() care citeste cuvintele dintr-un fisier text (words.txt) si gaseste TOATE cuvintele de lungime maxima (daca exista mai mult de unul) si le returneaza pe toate ca o lista de valori string.

# Indiciu: se poate rezolva in mai multe moduri:

# Solutia 1: cititi fisierul de doua ori:

# prima data: pentru a gasi lungimea maxima a cuvintelor (puteti refolosi si functia de la b) impreuna cu len); veti obtine lungimea, de ex 21
# a doua oara: luam din fisier doar cuvintele cu lungimea egala cu lungimea maxima gasita si le adaugam in lista de returnat la final
# Solutia 2, mai eficienta: citim fisierul o singura data, si pentru fiecare cuvant verificam:

# daca este la fel de lung ca unul din cuvintele cele mai lungi gasite pana acum (retinute intr-o lista), il adaugam si pe el la acea lista
# daca este mai lung decat cuvintele din lista de cuvinte maxime, golim acea lista (cuvintele vechi nu mai sunt bune), si apoi adaugam doar noul cuvant in lista
# Exemple:

# print('Cele mai lungi din fisier:', cele_mai_lungi_din_fisier()) 
# # afiseaza: Cele mai lungi din fisier: ['electroencefalografie', 'incomprehensibilitate', 'interdisciplinaritate', 'multidimensionalitate', 'multidisciplinaritate', 'pluridimensionalitate', 'pluridisciplinaritate', 'supraconductibilitate', 'termoconductibilitate']

def cel_mai_lung(lista_cuvinte):
  cuvant_final = ''
  for cuvant in lista_cuvinte:
    if len(cuvant) > len(cuvant_final):
      cuvant_final = cuvant
  return cuvant_final


# cuvant = cel_mai_lung(['A', 'fost', 'odata', 'ca', 'niciodata', 'o', 'rata'])
# print(f'Cel mai lung: {cuvant}')  # afiseaza: Cel mai lung: niciodata

# cuvant = cel_mai_lung([])  # empty list
# print(f'Cel mai lung: {cuvant}')  # afiseaza: Cel mai lung:


def cel_mai_lung_din_fisier():
  cuvant_final = ''
  with open('./words.txt', 'r') as fisier:
    for linie in fisier:
      cuvant = linie.strip()
      if len(cuvant) > len(cuvant_final):
        cuvant_final = cuvant
    return cuvant_final


# cuvant = cel_mai_lung_din_fisier()
# print(f'Cel mai lung din fisier: {cuvant} ({len(cuvant)} litere)')
# afiseaza: Cel mai lung din fisier: electroencefalografie (21 litere)


def cele_mai_lungi_din_fisier():
  cuvinte_maxime = []
  lungime_maxima = 0
  
  with open("./words.txt", 'r') as fisier:
      for linie in fisier:
          cuvinte = linie.split()
          for cuvant in cuvinte:
              lungime_cuvant = len(cuvant)
              if lungime_cuvant > lungime_maxima:
                  cuvinte_maxime = [cuvant]
                  lungime_maxima = lungime_cuvant
              elif lungime_cuvant == lungime_maxima:
                  cuvinte_maxime.append(cuvant)
  
  return cuvinte_maxime


print('Cele mai lungi din fisier:', cele_mai_lungi_din_fisier()) 
# afiseaza: Cele mai lungi din fisier: ['electroencefalografie', 'incomprehensibilitate', 'interdisciplinaritate', 'multidimensionalitate', 'multidisciplinaritate', 'pluridimensionalitate', 'pluridisciplinaritate', 'supraconductibilitate', 'termoconductibilitate']