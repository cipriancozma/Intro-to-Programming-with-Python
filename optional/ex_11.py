# Cuvinte palindrom din fisier
# Cititi toate cuvintele dintr-un fisier text (words.txt) si afisati doar cele care sunt cuvinte palindrom si care au mai mult de 3 litere. Afisati la final si numarul lor.

# Indiciu: puteti folosi functia palindrom() din tema anterioara, sau puteti reimplementa o versiune scurta a ei, bazata pe string slicing sau pe folosirea functiilor predefinite reverse si join
# Exemplu:

# cuvinte_palindrom_din_fisier()

def cuvinte_palindrom_din_fisier():
    count = 0
    with open('./words_ro.txt') as fisier:
        for cuvant in fisier:
            cuvant_striped = cuvant.strip()
            cuvant_reversed = ''.join(reversed(cuvant_striped))
            
            if len(cuvant_striped) > 3 and cuvant_striped == cuvant_reversed:
                count += 1
                print(cuvant_striped)
    print("Cuvinte palindrom gasite: ", count) 


cuvinte_palindrom_din_fisier()