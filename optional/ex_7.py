# Palindrom
# Pentru un cuvant dat (o valoare string), verificati daca este palindrom, adica daca este acelasi citit invers.

# a) Implementati mai intai o solutie bazata pe inversarea cuvantului (folosind functia de la exercitiul anterior, sau cu string slicing)

# b) Puteti gasi si o alta solutie? (una mai eficienta, care nu necesita inversarea cuvantului)

# Exemple:

# print(palindrom("rotitor"))  # True
# print(palindrom("abcdef"))  # False

def palidrom(txt):
    txt_nou = txt[::-1]
    return txt == txt_nou


print(palidrom('rotitor')) 
print(palidrom("abcdef"))