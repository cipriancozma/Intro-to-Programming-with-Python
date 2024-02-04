# Factorial (recursiv)
# Fiind dat un numar n (un intreg pozitiv), calculati valoare functiei 'factorial' pentru el, definita in matematica ca produsul tuturor numerelor intre 1 si n: fact(n) = 1*...*n

# Folositi o functie recursiva pentru rezolvare, bazata pe observatia ca factorial se poate defini si astfel:

# factorial(n) = n * factorial(n-1) (pasul de recursie)
# factorial(1) = 1 (conditia de oprire)
# Exemple:

# print(factorial(5)) # 120
# print(factorial(10)) # 3628800

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
print(factorial(10))