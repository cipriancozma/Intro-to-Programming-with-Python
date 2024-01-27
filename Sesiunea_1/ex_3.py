# Conversie timp (30p, a/b=10/20)
# a) Cititi de la utilizator 3 numere intregi - h,m,s - care reprezinta impreuna lungimea unui interval de timp, exprimata in ore, minute si secunde. Calculati si tipariti lungimea acestui interval exprimata in milisecunde.

# Exemplu:

# Introduceti orele: 1
# Introduceti minutele: 2
# Introduceti secundele: 3
# Lungimea intervalului este: 3723000 ms
# b) Cititi de la utilizator un numar intreg, care reprezinta lungimea unui interval de timp exprimata in secunde. Convertiti aceasta valoare la un numar de ore, minute si secunde (cu valorile pentru minute si secunde in intervalul lor normal 0..59), si tipariti aceasta valoare, in formatul: h:m:s

# Exemple:

# Introduceti nr de secunde: 7
# Lungimea intervalului este: 0:0:7

# Introduceti nr de secunde: 65
# Lungimea intervalului este: 0:1:5

# Introduceti nr de secunde: 2300
# Lungimea intervalului este: 0:38:20

# Introduceti nr de secunde: 7555
# Lungimea intervalului este: 2:5:55
# Indicii: cititi despre operatorii % si // din Pyton

h = int(input("Introduceti orele: "))
m = int(input("Introduceti minutele: "))
s = int(input("Introduceti secundele: "))
lungime_interval = (h * 3600 + m * 60 + s) * 1000
print(f"Lungimea intervalului este: {lungime_interval} ms")

numar_secunde = int(input("Introduceti nr de secunde: "))
ore = numar_secunde // 3600
minute = (numar_secunde % 3600) // 60
secunde = numar_secunde % 60
print(f"Lungimea intervalului este: {ore}:{minute}:{secunde}")