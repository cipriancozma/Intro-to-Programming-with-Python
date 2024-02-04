# Primele cuvinte din fisier
# Va este dat un fisier text ('words_ro.txt'), care contine cate un cuvant pe fiecare linie. Cititi un numar intreg n de la utilizator, si apoi afisati primele n cuvinte din fisier, toate pe o singura linie, separate de spatii.

# Exemplu:

# n = int(input("Introduceti nr de linii: "))
# primele_cuvinte_din_fisier(n)  # primele 7 cuvinte din fisier: aalenian abac abaca abacterian abager abagerie abagiu

n = int(input("Introduceti nr de linii: "))

def primele_cuvinte_din_fisier(n):
    with open('./words_ro.txt') as fisier:
        for i in range(n):
            linie = fisier.readline()
            print(linie.strip())

primele_cuvinte_din_fisier(n)