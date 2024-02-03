# Ziua din saptamana
# Fiind dat numele unei zile din saptamana, afisati pozitia ei in saptamana, ca un numar intre 1 si 7 (1 fiind luni), sau valoarea -1 daca numele este invalid.

# Nota: numele zilei e considerat corect indiferent cum e scris, cu litere mari si/sau mici.

# Indiciu: incepeti cu o versiune mai simpla care recunoaste doar numele cu litere mici, si ganditi-va dupa cum o puteti extinde sa recunoasca orice fel de litere; cititi de asemenea despre functiile upper()/lower() disponibile pentru valori tip string.

# Exemple:

# Introdu numele zilei: luni
# Numarul zilei: 1    

# Introdu numele zilei: JOI
# Numarul zilei: 4

# Introdu numele zilei: DuMiNiCa
# Numarul zilei: 7

# Introdu numele zilei: maine
# Numarul zilei: -1

zi = input("Introdu numele zilei: ").lower()
zile_saptamana = {
    "luni": 1,
    "marti":2,
    "miercuri": 3,
    "joi": 4,
    "vineri": 5,
    "sambata": 6,
    "duminica": 7
}

def saptamana(zile_saptamana):
    for cheie, valoare in zile_saptamana.items():
        if zi == cheie:
            return valoare
       
    return -1

print(saptamana(zile_saptamana))