zbior=10000       #przeszukiwany zbiór 
primetab=[0]        #tablica z liczbami pierwszymi
kon_szuk=0          #marker dzialania petli
i=0
n=2
licznik=0           #licznik do zliczania dzielnikow
index=0             #index tablicy liczb pierwszych
ostp=0

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
                primetab.append(n)
                index=index+1
                licznik=0
                
                
        if i == zbior-1:
            kon_szuk=1
            ostp=primetab[-1]
            break;


suma=0
for n in range(0, len(primetab)):
    suma=suma+primetab[n]
    

#print (primetab)
print (ostp,suma)
