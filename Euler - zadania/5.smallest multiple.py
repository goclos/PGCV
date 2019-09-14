#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
wiedwu=[1]
for i in range (11000000, 15000000):#petla do zmniejszenia liczby przeszukiwanych elementow. Generuje zbior do przeszukiwania podielny przez 20
    
    wiedwu.append(20*i)
    
    
print(wiedwu[len(wiedwu)-1])#wartosc ostatniego elementu zbioru do przeszkiwania

tabdzielaca=[11,12,13,14,15,16,17,18,19]
#9



licznik=0
for n in range(0, len(wiedwu)-1):
    for i in range(0,9):
        wynik = wiedwu[n]/tabdzielaca[i]
        if wynik.is_integer():
            licznik=licznik+1
            if licznik==9:
                print(wiedwu[n])
                break
    #print (licznik)
    licznik=0






