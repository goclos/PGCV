
def policz_potege_liczby_dwa(n):
    wynik = 2**n
    return wynik

def suma_cyfr_liczby(liczba):
    liczba_str = str(liczba)
    suma=0
    for i in range(0, len(liczba_str)):
        suma = suma + int(liczba_str[i])
    return suma


wynik = policz_potege_liczby_dwa(1000)

print(suma_cyfr_liczby(wynik))
