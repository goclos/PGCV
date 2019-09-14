import sys
from random import randint
widok=[]# tu będzie przechowywany widok planszy
trescpusta=['[]','[]','[]','[]','[]','[]','[]','[]','[]']
widok=trescpusta
koniec=False
kto=0

def drukuj(tab):
    kon=False
    leg=['1','2','3','4','5','6','7','8','9']
    print("Legenda:       Gra:")#drukuje legende
    for katy in range(0,9):     #petla czyszczoca nawiasy kwadrtowe, aby gra sie ladnie wyswietlala
        if tab[katy] == "X" or tab[katy] =="O":
            for nty in range(0,9):
                if tab[nty] == "[]":
                    tab[nty] = " "
                    kon = True
        if kon:
            break
    kon = False
    print ("%s | %s | %s     %s | %s | %s" % (leg[0],leg[1],leg[2],tab[0],tab[1],tab[2]))#drukuje pierwsza linie
    print ("%s | %s | %s     %s | %s | %s" % (leg[3],leg[4],leg[5],tab[3],tab[4],tab[5]))#drukuje druga linie
    print ("%s | %s | %s     %s | %s | %s" % (leg[6],leg[7],leg[8],tab[6],tab[7],tab[8]))#drukuje trzecia linie
    
def sprawdz(tab):#sprawdza kto wygrywa
    licz=0
    koniec=False
    if tab[0]==tab[1]==tab[2]!='[]' and tab[0]!=' ':
        koniec=True
        print ("Brawo! Wygrał '%s'" % (tab[0]))
    if tab[3]==tab[4]==tab[5]!='[]' and tab[3]!=' ':
        koniec=True
        print ("Brawo! Wygrał '%s'" % (tab[3]))
    if tab[6]==tab[7]==tab[8]!='[]' and tab[6]!=' ':
        koniec=True
        print ("Brawo! Wygrał '%s'" % (tab[6]))
    if tab[0]==tab[3]==tab[6]!='[]' and tab[0]!=' ':
        koniec=True
        print ("Brawo! Wygrał '%s'" % (tab[0]))
    if tab[1]==tab[4]==tab[7]!='[]' and tab[1]!=' ':
        koniec=True
        print ("Brawo! Wygrał '%s'" % (tab[1]))
    if tab[2]==tab[5]==tab[8]!='[]' and tab[2]!=' ':
        koniec=True
        print ("Brawo! Wygrał '%s'" % (tab[2]))
    if tab[0]==tab[4]==tab[8]!='[]' and tab[0]!=' ':
        koniec=True
        print ("Brawo! Wygrał '%s'" % (tab[0]))
    if tab[2]==tab[4]==tab[6]!='[]' and tab[2]!=' ':
        koniec=True
        print ("Brawo! Wygrał '%s'" % (tab[2]))
    for n in range(0,9):
        if tab[n] == ' ':
            licz = licz +1
    if licz == 0:
        print("Remis! Spróbujcie jeszcze raz!")
        koniec = True
        
    return koniec
        
    
def read():#funkcja musi wczytać wsp X lub O i sprawdzić czy dane są dobre i czy dana wsp nie zostala juz podana!
    global widok    
    global kto      #kogo ruch, 0= kółko, 1= krzyzyk
    marker=1        #Wykonywanie petli
    licznik=0       #licznik sprawdzajacy czy podana cyfra miesci się z zakresie wsp.
    if kto==0:
        while marker==1:
            ko= input("Podaj liczbę od 1 do 9 gdzie chcesz postawić 'O':")
            for index in range(1,10):#sprawdzam czy liczba mieści się w zakresie
                if int(ko)== index:
                    licznik=licznik+1
            if licznik<1:               #Liczba jest poza zakresem
                print("Liczba poza zakresem! podaj cyfrę od 1 do 9")
            
            if licznik==1:              #Liczba ok, ale...
                marker=0
                if widok[int(ko)-1]!="[]" and widok[int(ko)-1]!=" ":  #Jesli wsp juz była już wybrana to trzeba podac inna
                    print ("Tu już był O/X! Wybierz inne miejsce!")
                    marker=1
            licznik=0
            
        widok[int(ko)-1]="O"
        kto=1
        return widok
    
    if kto==1:
        while marker==1:
            kr= input("Podaj liczbę od 1 do 9 gdzie chcesz postawić 'X':")
            for index in range(1,10):#sprawdzam czy liczba mieści się w zakresie
                if int(kr)== index:
                    licznik=licznik+1
            if licznik<1:               #Liczba jest poza zakresem
                print("Liczba poza zakresem! podaj cyfrę od 1 do 9")
            
            if licznik==1:
                marker=0
                if widok[int(kr)-1]!="[]" and widok[int(kr)-1]!=" ":
                    print ("Tu już był O/X! Wybierz inne miejsce!")
                    marker=1
            licznik=0
            
        widok[int(kr)-1]="X"
        kto=0
        return widok
            

    

drukuj(trescpusta) #wydrukowanie pustej tabelki i legendy

kontrola = False

while koniec != True:
    widok=read()
    sprawdz(widok)
    drukuj(widok)
    

    
    if sprawdz(widok):
        sys.exit(0)
    
sys.exit(0)
