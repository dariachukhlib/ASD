#Zadanie 1
def fibonacci(n):
    fibArray = [0] * (n + 1)
    fibArray[0] = 0
    fibArray[1] = 1

    for i in range(2, n +1):
        fibArray[i] = fibArray[i - 1] + fibArray[i - 2]

    return fibArray[n]

n = 15
wynik = fibonacci(n)
print("Fibonacciego dla N = ", n, " wynik Fib(n) = ", wynik)


#Zadanie 3
def function(n):
    wyrazy = [0] * (n + 1)
    wyrazy[0] = 1
    wyrazy[1] = 1

    for i in range(2, n + 1):
        wyrazy[i] = 2 * wyrazy[i - 1] - wyrazy[i - 2]

    return wyrazy[n]

n = 5
wynik = function(n)
print("Rekurencyjna funkcja z zadania 3 dla N = ", n, "wynik f(n) = ", wynik)


#Zadanie 4
def wspolczynnikDwumianowy(n, m):
    tablica = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n+1):
        tablica[i][0] = 1

    # Obliczamy wartości zgodnie z równaniem rekursji dla symbolu newtona
    for i in range(1, n+1):
        for j in range(1, m+1):
            tablica[i][j] = tablica[i-1][j-1] + tablica[i-1][j]

    return tablica[n][m]

n = 15
m = 4
wynik = wspolczynnikDwumianowy(n, m)
print("Symbol Newtona dla n =", n, "i m =", m, "równa się:", wynik)

