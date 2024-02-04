# Suma patratelor (recursiv)
# Fiind dat un numar n (un intreg pozitiv), calculati suma patratelor tuturori numerelor intre 1 si n: suma_patrate(n) = 1*1 + 2*2+ ... + n*n

# Indiciu: folositi o functie recursiva, construita pe baza observatiei ca:

# suma_patrate(n) = n*n + suma_patrate(n-1)
# suma_patrate(1) = 1
# Exemple:

# print(suma_patrate(3))
# print(suma_patrate(5)) 

def suma_patrate(n):
    if n == 1:
        return 1
    else:
        return n * n + suma_patrate(n - 1)
    
print(suma_patrate(3))
print(suma_patrate(5))