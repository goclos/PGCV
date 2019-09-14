#Zadanie główne: Jaka jest liczba trójkątna która ma ponad 500 czynników?
#Taski:
#Generowanie liczb trójkątnych
#Generowanie czynników liczb trójkatnych
zred_zbior=[0]
for i in range (1,2000000):#zmniejszenie zbioru liczb do liczb kwadratow podzielnych przez 10
    zred_zbior.append(i*10)

print (zred_zbior[150000])

zbior=1000       #przeszukiwany zbiór
pocz_zbioru=1
primetab=[0]        #tablica z liczbami pierwszymi
kon_szuk=0          #marker dzialania petli
trojkat=0           #aktualny trojkat
licznik=0           #licznik czynnikow

while kon_szuk==0:
    for i in range(1, zbior):           #szukamy w całym zbiorze
        for n in range(1,i):            #szukamy trojkatow
            trojkat=trojkat+n
            licznik=0
            for k in range(1, trojkat):  #sprawdzamy czynniki kazdego trojkata
                wynik=0
                wynik = trojkat / k
                if wynik.is_integer():  #jesli dane k jest dzielnikiem trojkata to +1 licznik
                    licznik=licznik+1
                    
        if licznik+1>20: 
            print(trojkat, licznik+1)
        trojkat=0
    kon_szuk=1

        
        
       
    
