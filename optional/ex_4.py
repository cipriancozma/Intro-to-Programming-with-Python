# Desenare dreptunghi
# Scrieti o metoda dreptunghi(linii,coloane) care afiseaza pe ecran un dreptunghi format prin repetarea unui caracter (#) pe numarul specificat de linii si coloane.

# Nota: desi numarul de linii si coloane nu e fix, nu aveti nevoie sa folositi aici inca bucle, exista solutii bazate doar pe expresii si operatori invatati pana acum (ex: *)

# Indicii:

# Ganditi-va mai intai cum puteti reprezenta o singura linie, care sa repete caracterul de numarul necesar de ori, si cum puteti termina linia (vezi caracterul dedicat pentru sfarsit de linie: '\n')

# Puteti 'impacheta' codul de mai sus intr-o metoda noua, linie(lungime) care primeste ca parametru un numar si intoarce linia ca o valoare tip string (incuzand si terminatorul de linie)

# Definiti apoi metoda dreptunghi, gandindu-va cum puteti refolosi metoda linie() pentru a crea un dreptunghi cu numarul necesar de linii (care poate fi memorat tot intr-o singura variabila tip string, si poate fi usor afisat dupa)

# Exemplu: dreptunghi(3, 20) va afisa:

# ####################
# ####################
# ####################

def linie_d(lungime):
    return lungime * '#'


def dreptunghi(linii, coloane):
    linie_dreptunghi = linie_d(linii)
    for lin in linie_dreptunghi:
        print(lin * coloane) 

dreptunghi(4, 10)