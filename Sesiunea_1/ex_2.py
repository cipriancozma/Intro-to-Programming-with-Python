# Convertor lungime (25p)
# a) Cititi de la utilizator un numar (de tip float) care reprezinta o distanta in kilometrii, transformati valoarea in mile si afisati-o.

# Exemplu:

# Introduceti distanta in km:  32.2
# Distanta in mile:  20.0
# b) Cititi de la utilizator un numar (de tip float) care reprezinta o distanta in mile, transformati valoarea in kilometrii si afisati-o.

# Exemplu:

# Introduceti distanta in mile:  4.5
# Distanta in km:  7.245
# Indiciu: 1 mila are 1.61 km; puteti declara in cod o constanta care sa memoreze aceasta valoare (de exemplu: KM_PE_MILA = 1.61) si apoi sa o folositi in calcule atat la punctul a) cat si la b). Incercati de asemenea sa folositi nume clare/sugestive pentru variabile, asa incat codul sa fie usor de citit.

MILA_PE_KM = 0.621371
distanta_km = float(input("Introduceti distanta in km: "))
distanta_mile = distanta_km * MILA_PE_KM
print(f"Distanta in mile: {distanta_mile:.2f}")

KM_PE_MILA = 1.61
distanta_mile_2 = float(input("Introduceti distanta in mile: "))
distanta_km_2 = distanta_mile_2 * KM_PE_MILA
print(f"Distanta in km: {distanta_km_2:.2f}")