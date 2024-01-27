# Verificare ordine (15p)
# a) Cititi de la utilizator 2 numere si verificati daca sunt date in ordine crescatoare sau sunt egale, si afisati True in acest caz, altfel False

# Exemple:

# Introduceti nr 1: 3
# Introduceti nr 2: 1
# Cele 2 numere sunt crescatoare sau egale ?: False

# Introduceti nr 1: 2
# Introduceti nr 2: 2
# Cele 2 numere sunt crescatoare sau egale ?: True

# Introduceti nr 1: 2
# Introduceti nr 2: 3
# Cele 2 numere sunt crescatoare sau egale ?: True
# b) Cititi de la utilizator 3 numere (a,b,c), verificati daca sunt toate ordonate - toate strict crescator sau toate strict descrescator - si in oricare din aceste doua cazuri afisati True (altfel False)

# Exemple:

# Introduceti nr 1: 1
# Introduceti nr 2: 4
# Introduceti nr 3: 4
# Cele 3 numere sunt ordonate strict ?: False

# Introduceti nr 1: 1
# Introduceti nr 2: 7
# Introduceti nr 3: 5
# Cele 3 numere sunt ordonate strict ?: False 

# Introduceti nr 1: 1
# Introduceti nr 2: 4
# Introduceti nr 3: 5
# Cele 3 numere sunt ordonate strict ?: True

# Introduceti nr 1: 9
# Introduceti nr 2: 7
# Introduceti nr 3: 3
# Cele 3 numere sunt ordonate strict ?: True 
# Indiciu: pentru a rezolva acest exercitiu, nu aveti nevoie de instructiuni conditionale (if-else), ci ar trebui sa folositi doar operatori (de comparatie sau logici: ==, <, <=, >, >=, and, or, not … )
num_1 = int(input("Introduceti nr 1: "))
num_2 = int(input("Introduceti nr 2: "))
rezultat = num_1 <= num_2
print(f"Cele 2 numere sunt crescatoare sau egale?: {rezultat} ")

numar_1 = int(input("Introduceti nr 1: "))
numar_2 = int(input("Introduceti nr 2: "))
numar_3 = int(input("Introduceti nr 3: "))
rezultat_crescator = numar_1 < numar_2 < numar_3
rezultat_descrescator = numar_1 > numar_2 > numar_3
rezultat = rezultat_crescator or rezultat_descrescator
print(f"Cele 3 numere sunt ordonate strict?: {rezultat}")

