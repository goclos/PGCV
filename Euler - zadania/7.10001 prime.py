#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
zbior=10000000       #przeszukiwany zbiór 
primetab=[0]        #tablica z liczbami pierwszymi
primecount=10001     #ile ma znaleźć liczb pierwszych
kon_szuk=0          #marker dzialania petli
i=0
n=2
licznik=0           #licznik do zliczania dzielnikow
index=0             #index tablicy liczb pierwszych

while kon_szuk==0:
    for i in range(2, zbior):
        licznik=0
        for n in range(2,i+1):
            wynik = 0
            wynik = i/n
            
            if wynik.is_integer():
                licznik=licznik+1

            if licznik > 1: #dana liczba jest sprawdzana dopóki ilość dzielników 
                licznik=0
                break
            
            if licznik==1 and i==n:#liczba jest pierwszą
                print(index,n)
                primetab.append(n)
                index=index+1
                licznik=0
        if index == primecount:
            #print(primetab)
            print(primecount," liczba pierwsza to: ",primetab[primecount])
            kon_szuk=1
            break;
        if i==zbior-1:
            print("koniec zbioru...")
            kon_szuk=1
        
#1Pomysł!!! zmodyfikować algorytm aby sprawdzał daną liczbę dopóki licznik jest mniejszy od 2
#2POMYSŁ!!!! Może ograniczyć przeszukiwany zbiór z liczb które są podzielne przez 2,3, 5, 
