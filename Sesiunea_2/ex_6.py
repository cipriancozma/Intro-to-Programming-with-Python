# Verificare triunghi (25p: a=10,b=15)
# a) Scrieti o functie numita verifica_triunghi(a,b,c) care primeste ca parametrii 3 numere (posibil cu virgula) care reprezinta lungimile unor segmente, si verifica daca ele pot forma laturile unui triunghi sau nu, returnand unul din mesajele: 'triunghi valid' sau 'triunghi invalid'

# Nota: pentru a putea forma un triunghi valid, laturile trebuie sa respecte regula generala: 'lungimea oricarei laturi trebuie sa fie mai mica decat suma celorlalte doua' (si regula suplimentara: 'lungimea laturilor trebuie sa fie strict mai mare ca zero')

# Exemple:

# print(verifica_triunghi(1, 10, 1))  # afiseaza: 'triunghi invalid'
# print(verifica_triunghi(-1, 2, 2))   # afiseaza: 'triunghi invalid'
# print(verifica_triunghi(3, 4, 5))   # afiseaza: 'triunghi valid'
# b) Optional: modificati functia anterioara astfel incat in cazul in care pot forma un triunghi valid, sa determine si tipul triunghiului, intorcand in loc de 'triunghi valid' una dintre valorile mai specifice:

# 'triunghi echilateral' (daca are toate laturile egale)
# 'triunghi dreptunghic' (pentru aceasta verificare puteti folosi teorema lui Pitagora in acest mod: daca patratul unei laturi este egal cu suma patratelor celorlalte doua laturi, atunci e dreptunghic...)
# 'triunghi oarecare' (pentru restul cazurilor)
# Exemple:

# print(verifica_triunghi(1, 2, 4))  # afiseaza: 'triunghi invalid'
# print(verifica_triunghi(3, 3, 3))  # afiseaza: 'triunghi echilateral'
# print(verifica_triunghi(8, 10, 6)) # afiseaza: 'triunghi dreptunghic'
# print(verifica_triunghi(6, 4, 4))  # afiseaza: 'triunghi oarecare'

def verifica_triunghi(a, b, c):
  if a > 0 and b > 0 and c > 0:
    if a < b + c and b < c + a and c < a + b:
      if a == b == c:
        return 'triunghi echilateral'
      elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + c**2:
        return 'triunghi dreptunghic'
      else:
        return 'triunghi oarecare'
    else:
      return 'triunghi invalid'
  else:
    return 'triunghi invalid'
    
# print(verifica_triunghi(1, 10, 1))
# print(verifica_triunghi(-1, 2, 2)) 
# print(verifica_triunghi(3, 4, 5)) 

print(verifica_triunghi(1, 2, 4))  # afiseaza: 'triunghi invalid'
print(verifica_triunghi(3, 3, 3))  # afiseaza: 'triunghi echilateral'
print(verifica_triunghi(8, 10, 6)) # afiseaza: 'triunghi dreptunghic'
print(verifica_triunghi(6, 4, 4))  # afiseaza: 'triunghi oarecare'