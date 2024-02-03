# Validare parola
# Cititi de la utilizator o valoare string, care reprezinta o parola. Verificati ca parola are o lungime valida, afisand unul din aceste mesaje:

# 'Parola e prea scurta' - daca are mai putin de 3 caractere
# 'Parola e prea lunga' - daca are mai mult de 8 caractere
# 'Parola e valida' - daca are intre 3 si 8 caractere

parola = input("Introdu parola: ")

if parola.isalpha() or parola.isnumeric():
    print("Parola e prea simpla")
elif len(parola) < 3:
    print("Parola e prea scurta")
elif len(parola) > 8:
    print("Parola e prea lunga")
elif 3 <= len(parola) <= 8:
    print("Parola e valida")