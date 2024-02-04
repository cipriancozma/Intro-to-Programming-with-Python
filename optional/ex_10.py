# Numarare cuvinte din fisier
# Scrieti o functie numar_cuvinte(lung_min,lung_max) care primeste ca parametrii 2 numere intregi, apoi citeste toate cuvintele dintr-un fisier text (words.txt) si numara cate dintre ele au lungimea intre cele 2 limite date, si intoarce acest numar total de cuvinte.

# Exemplu:

# print(numar_cuvinte(3, 5))  # 6468
# print(numar_cuvinte(10, 12))  # 12538
# print(numar_cuvinte(21, 25))  # 9

def numar_cuvinte(lung_min, lung_max):
    count = 0
    with open('./words_ro.txt') as fisier:
        for cuvant in fisier:
            cuvant_striped = cuvant.strip()
            if lung_min <= len(cuvant_striped) <= lung_max:
                count += 1
    return count



print(numar_cuvinte(3, 5))  # 6468
print(numar_cuvinte(10, 12))  # 12538
print(numar_cuvinte(21, 25))  # 9