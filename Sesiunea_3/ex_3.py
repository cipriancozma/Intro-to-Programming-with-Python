# Ion vrea sa faca un depozit la banca sa, si se intreaba in cati ani va obtine o suma totala dorita de el, luand in considerare dobanda acumulata anual.

# Scrieti o functie care sa il ajute sa simuleze diferite scenarii, si sa afle in cati ani se poate pensiona linistit :)

# Declaratia functiei: simulare(suma_initiala, procent_dobanda, suma_dorita)

# suma_initiala - suma initiala adaugata in depozit la creare
# procent_dobanda - dobanda anuala, exprimata ca procent (de ex, '2.5' inseamna 2.5%, adica 0.025 din suma)
# nota: dobanda este cumulativa - valoarea ei este calculata anual, bazat pe suma din depozit si pe procentul dobanzii, si apoi valoarea calculata se adauga sumei din cont si are efect pentru anul viitor
# suma_dorita - suma finala dorita de Ion
# Simularea ar trebui:

# sa calculeze dobanda si noua valoarea totala dupa fiecare an, si sa afiseze clar aceste valori (inclusiv numarul anului)
# sa se opreasca cand valoarea totala atinge sau depaseste suma dorita
# sa returneze ca valoare finala numarul de ani necesari.
# Nota: pentru o afisare mai clara, incercati sa afisati numerele cu virgula rotunjite la doar 2 cifre zecimale. Puteti folosi metoda format() cu sintaxa '{:.2f}' pentru valorile de inlocuit in string, vezi detalii aici

# Exemple:

# print(simulare(1000, 10, 1500))  # afiseaza: 5
# print(simulare(1000, 2.5, 1500))  # afiseaza: 17
# print(simulare(1000, 0.5, 1500))  # afiseaza: 82
# print(simulare(1000, 10, 900))  # afiseaza: 0
# Exemplu de afisare informatii extra: simulare(1000, 10, 1500) ar putea afisa:

# Parametrii simulare: suma_initiala= 1000, procent_dobanda= 10%, suma_dorita= 1500
#  - an 1: suma: 1000.00, dobanda: 100.00 => noua suma: 1100.00
#  - an 2: suma: 1100.00, dobanda: 110.00 => noua suma: 1210.00
#  - an 3: suma: 1210.00, dobanda: 121.00 => noua suma: 1331.00
#  - an 4: suma: 1331.00, dobanda: 133.10 => noua suma: 1464.10
#  - an 5: suma: 1464.10, dobanda: 146.41 => noua suma: 1610.51
# Te poti pensiona linistit in: 5 ani !

def simulare(suma_initiala, procent_dobanda, suma_dorita):
  an = 0
  noua_suma = suma_initiala
  while noua_suma < suma_dorita:
    dobanda_anuala = noua_suma * (procent_dobanda / 100)
    noua_suma += dobanda_anuala
    an += 1
    print("Anul {}: Suma totală = {:.2f}".format(an, noua_suma))
 
  print(f"Te poti pensiona linistit in: {an} {'ani' if an > 1 else 'an'}")


simulare(1000, 10, 1500)
simulare(1000, 2.5, 1500)
simulare(1000, 0.5, 1500)
simulare(1000, 10, 900)
