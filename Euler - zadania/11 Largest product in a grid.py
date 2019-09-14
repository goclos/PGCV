# Creates a list containing 5 lists, each of 8 items, all set to 0
import numpy as np
k=20
w=20
tab = [[0] * k] * w
file=open("11wsad.txt", "r")
tresc=file.read()
file.close()
posrednia=tresc.split()#przejscie ze stringa na tablice stringow

for i in range(0,len(posrednia)):#petla przechodzoca na tablice INT
    posrednia[i]=int(str(posrednia[i]))#tablica jednowymiarowa intow

c=0
r=0
licznik=0
      #przejscie na tablice 2 wymiarowa
for c in range(0,20):
    for r in range(0, 20):
        tab[c][r]=posrednia[licznik]
        #print (c, r, licznik, posrednia[licznik])
        licznik=licznik+1
    
        
    

print (posrednia,'\n')
#print (tab[1][1])
sumc=0
a=b=c=d=0


najwieksza=0
#sasiedzi poziomo

ilocz=1 #iloczyn sasiadow
sas=4   #ilosc sasiadow poziomo
x=1     #zmienna pomocnicza do liczenia 
for index in range(0, 400):     #Przeszukaj pełen zakres tablicy
    for e in range(0,sas):      #ile sasiadow?
        
        if  index>=(20*x)-3 and index<=(20*x)-1:#odciecie regionu poszukiwan do od 0 do 15
            if index>20*x:    #zwiekszanie zmiennej pomocniczej. Jest to krotnosc 20, czyli wiersza 
                x=x+1
            break
        
        if index+sas<=399:        #Jesli ineks + tymczasowa wsp. jest mniejsza niż indeks ostatniego elem.
            ilocz=ilocz*posrednia[index+e]
            if najwieksza<ilocz:    #szukanie najwiekszej
                najwieksza=ilocz
                a=posrednia[index]
                b=posrednia[index+1]
                b=posrednia[index+2]
                d=posrednia[index+3]
                
                #print(posrednia[index], posrednia[index+1],posrednia[index+2],posrednia[index+3],ilocz)

        else:
            break
        
        
                    
        if e==3:
            #print(posrednia[index], posrednia[index+1],posrednia[index+2],posrednia[index+3],ilocz)
            ilocz=1

print("\n","Najwiekszy iloczyn poziomo: ",najwieksza)

#Sasiedzi pionowo

najwieksza=0
#sasiedzi poziomo

ilocz=1 #iloczyn sasiadow
sas=4   #ilosc sasiadow poziomo
x=1     #zmienna pomocnicza do liczenia 
for index in range(0, 400):     #Przeszukaj pełen zakres tablicy
    for e in range(0,sas):      #ile sasiadow?
        
        if  index>=340:#odciecie regionu poszukiwan do od 0 do 15
            break
        
        if index+sas<=399:        #Jesli ineks + tymczasowa wsp. jest mniejsza niż indeks ostatniego elem.
            ilocz=ilocz*posrednia[index+(e*20)]
            
            if najwieksza<ilocz:    #szukanie najwiekszej
                najwieksza=ilocz
                #print(posrednia[index], posrednia[index+20],posrednia[index+40],posrednia[index+60],ilocz)

        else:
            break
        
        
                    
        if e==3:
            #print(posrednia[index], posrednia[index+20],posrednia[index+40],posrednia[index+60],ilocz)
            ilocz=1

print("\n","Najwiekszy iloczyn pionowo: ",najwieksza)


#Sasiedzi po przekatnej w prawo
najwieksza=0
ilocz=1 #iloczyn sasiadow
sas=4   #ilosc sasiadow poziomo
x=1     #zmienna pomocnicza do liczenia

for index in range(0, 400):     #Przeszukaj pełen zakres tablicy
    for e in range(0,sas):      #ile sasiadow?
        
        if  index>=(20*x)-3 and index<=(20*x)-1:#odciecie regionu poszukiwan do od 0 do 15
            if index>20*x:    #zwiekszanie zmiennej pomocniczej. Jest to krotnosc 20, czyli wiersza 
                x=x+1
            break

        if index+(e*21)<400:
            ilocz=ilocz*posrednia[index+((e*21))]

        #print(e*21, posrednia[index+((e*21))],ilocz)
        if najwieksza<ilocz:    #szukanie najwiekszej
            najwieksza=ilocz
            #print(posrednia[index], posrednia[index+21],posrednia[index+42],posrednia[index+63],ilocz)

                    
        if e==3:
            
            #print(posrednia[index], posrednia[index+21],posrednia[index+42],posrednia[index+63],ilocz, index)
            ilocz=1

print("\n","Najwiekszy iloczyn po przekatnej w prawo: ",najwieksza)



#Sasiedzi po przekatnej w lewo
najwieksza=0
ilocz=1 #iloczyn sasiadow
sas=4   #ilosc sasiadow poziomo
x=1     #zmienna pomocnicza do liczenia

for index in range(0, 400):     #Przeszukaj pełen zakres tablicy
    for e in range(0,sas):      #ile sasiadow?
        
        if  index>=(20*x)-20 and index<=(20*x)-18:#odciecie regionu poszukiwan do poszukiwan
            if index>20*x:    #zwiekszanie zmiennej pomocniczej. Jest to krotnosc 20, czyli wiersza 
                x=x+1
            break
        if index+(19*e) < 369:
            ilocz=ilocz*posrednia[index+(19*e)]

        #print(e*21, posrednia[index+((e*21))],ilocz)
        if najwieksza<ilocz:    #szukanie najwiekszej
            najwieksza=ilocz
            #print(posrednia[index], posrednia[index+21],posrednia[index+42],posrednia[index+63],ilocz)

                    
        if e==3:
            
            #print(posrednia[index], posrednia[index+21],posrednia[index+42],posrednia[index+63],ilocz, index)
            ilocz=1

print("\n","Najwiekszy iloczyn po przekatnej w lewo: ",najwieksza)
