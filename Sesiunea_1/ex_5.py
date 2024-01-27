# Aceeasi lungime (10p)
# Cititi de la utilizator 2 fragmente de text (ca valori de tip string), apoi afisati lungimea in caractere a fiecaruia, si de asemenea valoarea True daca au aceeasi lungime, sau False in caz contrar.

# Exemple:

# Introduceti primul text: Cristi
# Introduceti al doilea text: Alex
# Lungime texte: 6 4.  Au aceeasi lungime?: False

# Introduceti primul text: Oana
# Introduceti al doilea text: Alex
# Lungime texte: 4 4.  Au aceeasi lungime?: True

text_1 = len(input("Introduceti primul text: "))
text_2 = len(input("Introduceti al doilea text: "))
rezultat = text_1 == text_2
print(f"Lungime texte: {text_1} {text_2}: Au aceeasi lungime?: {rezultat}")