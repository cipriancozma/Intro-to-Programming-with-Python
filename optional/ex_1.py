# Pret final
# Un magazin vinde un produs cu aceasta promotie: pretul intreg al produsului este P, 
# dar cand cumperi doua primesti 50% reducere pentru al doilea produs.

# Vrei sa cumperi N bucati din acel produs. Care e suma totala pe care trebuie sa o platesti?

# Nota: valorile pentru P, N vor fi citite de la utilizator

# Exemplu:

# Introdu pretul intreg (pe bucata): 10
# Introdu numarul de bucati cumparate: 5
# Suma totala de platit: 40.0

P = int(input("Introdu pretul intreg (pe bucata): "))
N = int(input("Introdu numarul de bucati cumparate: "))
reducere = 0.5

total_pairs = N // 2
remaining = N % 2
total = (total_pairs * (P + (P * 0.5))) + (remaining * P)

print(total)
