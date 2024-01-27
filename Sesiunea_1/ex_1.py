# Ipotenuza triunghi dreptunghic (20p)
# Fiind date lungime celor 2 laturi scurte (catete) ale unui triunghi dreptunghic (ca numbere cu virgula, de tip float), calculati si tipariti lungimea laturii lungi (ipotenuzei).

# Optional: incercati sa tipariti rezulatul ca un numar rotunjit doar la 2 zecimale.

# Exemple:

# Lungime cateta 1: 3.3
# Lungime cateta 2: 4.4
# Lugimea ipotenuzei este: 5.5

# Lungime cateta 1: 3
# Lungime cateta 2: 3
# Lugimea ipotenuzei este: 4.24
# Indicii:

# puteti folosi Teorema lui Pithagora pentru calcule

# pentru a calcula puterea a doua a unui numar, puteti folosi si operatorul ** (ca alternativa la a folosi doar x*x)

# pentru a calcula radacina patrata a unui numar:

# puteti folosi functia predefinita dedicata sqrt() ('square root'): trebuie mai intai sa importati modulul optional math si apoi puteti folosi functia:
# import math
# print( math.sqrt(5))
# alternativa: obtineti acelasi rezultat ridicand numarul la puterea 0.5 (=1/2)

import math

cateta_1 = float(input("Lungime cateta 1: "))
cateta_2 = float(input("Lungime cateta 2: "))

lungime_ipotenuza = math.sqrt(cateta_1**2 + cateta_2**2)

print(f"Lugimea ipotenuzei este: {lungime_ipotenuza:.2f}")


