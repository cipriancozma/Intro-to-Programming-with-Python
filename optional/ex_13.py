# Frecventa litere
# Scrieti o functie care primeste ca parametru un text, calculeaze numarul de aparitii al fiecarei litere din el si returneaza rezultatul sub forma unui dictionar, in care cheile sunt literele si valorile numarul de aparitii.

# Exemplu:

# print(frecventa_litere("abecedar"))  # {'a': 2, 'b': 1, 'e': 2, 'c': 1, 'd': 1, 'r': 1

def frecventa_litere(text):
    dictionar = {}
    for item in text:
        if item not in dictionar:
            dictionar[item] = 1
        else:
            dictionar[item] += 1
    return dictionar

print(frecventa_litere("abecedar"))