# Compactare lista cumparaturi
# Se da o lista de cumparaturi care contine linii de forma cafea,14, lapte,2. Numele aceluiasi produs poate aparea pe mai multe linii, cu numere diferite dupa.

# Sa se scrie o functie care citeste linie cu linie fisierul cu lista initiala, o analizeaza si compacteaza si returneaza un dictionar in care fiecare cheie reprezinta numele unui produs, iar valorile reprezinta numarul total de bucati ce trebuie cumparate din fiecare.

# Nota: lista initiala poate fi create si editata inclusiv dintr-un program gen Excel, daca va asigurati ca contine doar 2 coloane cu datele asteptate, si este salvat in formatul CSV (Comma Separated Values)
# Exemplu:

# continut fisier initial:
# oua,6
# inghetata,2
# faina,3
# carne,2
# oua,2
# inghetata,2
# lapte,2
# ciocolata,1
# carne,1
# ciocolata,2
# apa,3
# lapte,1
# faina,1
# rezultat rulare cod:
# print(lista_cumparaturi())  # {'oua': 8, 'inghetata': 4, 'faina': 4, 'carne': 3, 'lapte': 3, 'ciocolata': 3, 'apa': 3}

def lista_cumparaturi():
    dictionar = {}
    with open('./lista.csv', 'r', encoding='cp1252') as fisier:
        for linie in fisier:
            linie_striped = linie.strip().split(",")
            if len(linie_striped) == 2:
                cheie, valoare = linie_striped
                if cheie not in dictionar:
                    dictionar[cheie] = int(valoare)
                else:
                    dictionar[cheie] += int(valoare)
    return dictionar


print(lista_cumparaturi())
