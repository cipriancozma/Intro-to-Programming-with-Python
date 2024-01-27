# Fizz Buzz (15p)
# Scrieti o functie fizzbuzz(n) care primeste ca parametru un numar intreg si afiseaza un text, bazat pe aceste reguli:

# daca numarul e divizibil cu 3, afiseaza 'fizz'
# daca numarul e divizibil cu 5, afiseaza 'buzz'
# daca numarul e divizibil si cu 3 si cu 5, afiseaza 'fizzbuzz'
# altfel afiseaza numarul initial
# Observatie: functia nu trebuie sa returneze nimic, doar sa afiseze valoarea

# Exemple:

# fizzbuzz(6)   # afiseaza: 'fizz'
# fizzbuzz(20)  # afiseaza: 'buzz'
# fizzbuzz(30)  # afiseaza: 'fizzbuzz'
# fizzbuzz(7)   # afiseaza: '7'
# Nota: aceasta e o problema frecvent intalnita la interviurile pentru posturile de programatori juniori, pentru a verifica daca pot scrie o bucata simpla de cod; idea este ca ar trebui sa reuseasca sa scrie solutia direct pe hartie (ca pseudocod sau chiar cod corect) si sa fie corecta din prima, fara a o executa/verifica pe un calculator. Reusesti sa faci asta si tu? (sa scrii o solutie care sa mearga bine la prima incercare de rulare)

def fizzbuzz(n):
  if n % 3 == 0 and n % 5 == 0:
    return 'fizzbuzz'
  elif n % 3 == 0:
    return 'fizz'
  elif n % 5 == 0:
    return 'buzz'
  else:
    return n
  

print(fizzbuzz(6))
print(fizzbuzz(20))
print(fizzbuzz(30))
print(fizzbuzz(7))
