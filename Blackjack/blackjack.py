#Do zrobienia: ostatnio pracowałem nad RuchGracza(). Do zrobienia zostało sprawdzanie czy w kasie nie jest za mało oraz czy zakłady nie przekraczają kasy.
#No i Trzeba zrobić możliwośc zamknięcia gry.
import random
import os
import time


class Talia:
    def __init__(self):
        self.karty = ['2','3','4','5','6','7','8','9','10','J','D','K','A']    #Typ kart
        self.kolory = ['Kier','Pik','Trefl','Karo']    #kolory kart
        self.wartosciKart = {' ':0,'0':0,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'D':10,'K':10,'A':11}  #Wartosci kart w blackjack (nie używane)
        self.Talia = [[0]*52, [0]*52]#unikalna talia kart
        self.TaliaPotasowana = [[0]*52, [0]*52]
        self.KluczTasujacy = [0]*52 #służy do tasowania Talii kart
        self.Talia[0] = self.karty*4    #Stworzenie kolorow talii
        self.Talia[1] = self.kolory*13  #Stworzenie typoów kart w talii
        self.tempTalia = [[0]*52, [0]*52]   #Zmienna używana tylko w metodzie tasowania kart
        
        
        for i in range(0,52):   
            self.KluczTasujacy[i]=i  #przypisanie liczb od 0 do 51

        #print("Karty:\n {}".format(self.Talia))

        random.shuffle(self.KluczTasujacy)   #Tasowanie klucza

        for i in range(0,52):
            self.TaliaPotasowana[0][i] = self.Talia[0][self.KluczTasujacy[i-1]]
            self.TaliaPotasowana[1][i] = self.Talia[1][self.KluczTasujacy[i-1]]
        """
        for i in range(0,52):#sprawdzam czy jesto odpowiednia ilość  każdego typu karty
            for k in range(0,13):
                if TaliaPotasowana[0][i] == karty[k]:
                    print (TaliaPotasowana[0][i] , TaliaPotasowana[1][i],)
                        
        print("\nKolory\n")        
        for i in range(0,4):#sprawdzam czy jesto odpowiednia ilość  kolorow
            for k in range(0,52):
                if TaliaPotasowana[1][k] == kolory[i]:
                    print (TaliaPotasowana[1][k] , TaliaPotasowana[0][k])
        """
        
    def potasuj(self, doPrzetasowania):
        self.tempTalia = doPrzetasowania
        for i in range(0,52):
            self.TaliaPotasowana[0][i] = self.tempTalia[0][self.KluczTasujacy[i-1]]
            self.TaliaPotasowana[1][i] = self.tempTalia[1][self.KluczTasujacy[i-1]]


class Stol:
    def __init__(self, Talia):
        self.Talia = Talia              #Talia
        self.wartosciKart = {' ':0,'0':0,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'D':10,'K':10,'A':11}  #Wartosci kart w blackjack
        self.KartyGracza = [['0']*10, ['0']*10]    #Karty Gracza. Liczba ta oznacza maks. liczbę kart.
        self.KartyKrupiera = [['0']*10, ['0']*10]   #Karty Krupiera. Liczba ta oznacza maks. liczbę kart.
        self.LiczKartGracza = 0         #Ile kart ma gracz
        self.LiczKartKrupiera = 0       #Ile kart ma krupier
        self.WartoscGracza = 0          #Wartosc kart gracza
        self.WartoscKrupiera = 0        #Wartość kart Krupiera              
        self.nastGra = False
        self.start = True
        #self.start2 = True
        self.koniec = False             #Flaga dzięki której metoda ruch gracza może zostać przerwana, np. w skutek zakończenia partii - patrz metoda Sprawdź wynik
        self.kasa = 0
        self.zaklad = 0
        self.liczPobranychKart = 0      #Potrzebny do określania ile kart zostało pobranych z talii
        self.ruchGracza = " "
        self.liczAgracza = 0
        self.liczAkrupiera = 0
        self.wynik = "0"          #Zmienna przechowująca decyzje gracza po przegranej lub wygranej.
        os.system( 'cls' )
        print(" Witaj! Zagramjmy w BlackJack'a !")
        time.sleep(2)
        
    def __del__(self):
        pass

    def zerujWartosci(self):
        self.KartyGracza = [['0']*10, ['0']*10]    #Karty Gracza. Liczba ta oznacza maks. liczbę kart.
        self.KartyKrupiera = [['0']*10, ['0']*10]   #Karty Krupiera. Liczba ta oznacza maks. liczbę kart.
        self.LiczKartGracza = 0         #Ile kart ma gracz
        self.LiczKartKrupiera = 0       #Ile kart ma krupier
        self.WartoscGracza = 0          #Wartosc kart gracza
        self.WartoscKrupiera = 0        #Wartość kart Krupiera
        self.start = True              #Tej wartosci nie zeruje
        #self.start2 = True
        self.zaklad = 0
        self.liczPobranychKart = 0      #Potrzebny do określania ile kart zostało pobranych z talii
        self.ruchGracza = " "
        self.liczAgracza = 0
        self.liczAkrupiera = 0
        self.wynik = "0"   

                
    def Start(self):
        if self.kasa <=0:               #Jesli kasa =0 to wtedy zapytaj ile gracz chce do niej dorzucic
            self.dodajSrodki()
        """
        if self.nastGra == True: #Jeśli jest to następna partia gry, to nie wyświetlaj tekstu powitalnego z metody wys()
            pass        #nie wyświetlaj ekranu powitalnego
            
        else:
            self.wys()  #wyśw tekstu powitalnego
        """    
        self.nastGra = False 
        self.postawZaklad()
        self.noweRozdanie()
        self.wartoscKartKrupiera()
        self.wartoscKartGracza()
        self.wys()

    def RuchGracza(self):
        #self.wys()
        while True:
            self.ruchGracza = input("\n Hit (H) czy Stand (S). Naciśnij właściwą literę :")
            if self.ruchGracza != "s" and self.ruchGracza !=  "S" and self.ruchGracza !=  "H" and self.ruchGracza !=  "h":
                print(" Coś nie tak. Podaj 'H' lub 'S' ")
            else:
                #print("Jest break")
                break
            
        if self.ruchGracza == "H" or self.ruchGracza == "h":
            self.hit()
            self.wys()
            self.SprwadzWynik()
            
        elif self.ruchGracza == "S" or self.ruchGracza == "s":
            while True:             #Pętla po "Stand" w której "Krupier" dobiera sobie karty i są one wyświetlane w terminalu
                self.stand()
                self.wys()
                time.sleep(1)
                if self.WartoscKrupiera >= self.WartoscGracza:
                    self.SprwadzWynik()
                time.sleep(1)
                if self.wynik != "0":
                    break
                
                

        if self.wynik == "Wygrana" or self.wynik == "Przegrana" or self.wynik == "Remis":
            #print("print 666", "self.wynik", self.wynik)
            self.zerujWartosci()
            self.nastGra = True
            
            
                
            
    def postawZaklad(self):
        while True:
            os.system( 'cls' )#czyszczenie Termianala (działa w konsoli windows)
            print(" Twoje środki: ", self.kasa)
            self.zaklad = input(" Ile stawiasz? :")
            try:
                liczba = int(self.zaklad)
            except:
                print(" To nie jest liczba całkowita. Wprowadź poprawną wartość!")
                time.sleep(2)
                continue
            #if int(self.zaklad) <= 0:  #sprawdzam czy zakład nie jest mniejszy równyc 0
                print(" Zakład nie może być mniejszy niż '0'")
                continue
            
            if int(self.zaklad) > int(self.kasa):
                print(" Masz za mało środków na taki zakład...")
                time.sleep(2)                
            else:   #jesli zaklad nie jest wiekszy niz konto
                break 

        self.kasa = int(self.kasa) - int(self.zaklad)

    def dodajSrodki(self):
        while True:
            os.system( 'cls' )
            self.kasa = input(" Ile chcesz wprowadzić do kasy? :")
            try:
                liczba = int(self.kasa)
            except:
                print(" To nie jest liczba całkowita. Wprowadź poprawną wartość!")
                time.sleep(2)
                continue
            else:
                break
        print(" Zaczynamy!")
        time.sleep(1)
        #self.start = False

    def hit(self):
        #print("Hit zostało wywołane, self.LiczKartGracza:", self.LiczKartGracza, "self.KartyGracza:",self.KartyGracza)
        #print("Hit zostało wywołane, self.LiczKartKrupiera:", self.LiczKartKrupiera, "self.KartyKrupiera",self.KartyKrupiera )
        self.KartyGracza[0][self.LiczKartGracza] =  self.Talia[0][self.liczPobranychKart]   #Dadnie nowej karty graczowi
        self.KartyGracza[1][self.LiczKartGracza] =  self.Talia[1][self.liczPobranychKart]
        self.wartoscKartGracza()    
        self.wartoscKartKrupiera()
        #print("self.WartoscGracza:", self.WartoscGracza ,"self.WartoscKrupiera:", self.WartoscKrupiera )
        time.sleep(2)
        
    def stand(self):
        #print("Stand zostało wywołane")
        self.KartyKrupiera[0][self.LiczKartKrupiera] =  self.Talia[0][self.liczPobranychKart]   #Dadnie nowej karty graczowi
        self.KartyKrupiera[1][self.LiczKartKrupiera] =  self.Talia[1][self.liczPobranychKart]    
        self.wartoscKartGracza()
        self.wartoscKartKrupiera()  
        #print("self.WartoscGracza:", self.WartoscGracza ,"self.WartoscKrupiera:", self.WartoscKrupiera )
        time.sleep(2)
    
    def noweRozdanie(self):
        self.KartyGracza[0][0] = self.Talia[0][0]   #dla karty
        self.KartyGracza[1][0] = self.Talia[1][0]   #dla koloru
        self.KartyKrupiera[0][0] = self.Talia[0][1] #dla karty
        self.KartyKrupiera[1][0] = self.Talia[1][1] #dla koloru
        self.KartyGracza[0][1] = self.Talia[0][2]   #dla karty
        self.KartyGracza[1][1] = self.Talia[1][2]   #dla koloru
        self.KartyKrupiera[0][1] = self.Talia[0][3] #dla karty
        self.KartyKrupiera[1][1] = self.Talia[1][3] #dla koloru
        self.liczPobranychKart = 4    #zawsze po nowym pobraniu licznik pobrnych kart =4

    def wys(self):  #Czyszczenie i wyswietalanie Stolu
        self.licznikKart()
    
        if  self.start == False:   #Wyświetlanie po pierwym i następnych "Hit" lub "Stand"

            for i in range(0,10):   #Pętla do wyczyszczenia "pustych" miejsc w tablicy z kartami. Aby nie wyświetlały się "0"
                if self.KartyKrupiera[0][i] == '0':
                    self.KartyKrupiera[0][i] = ' '
                    self.KartyKrupiera[1][i] = ' '

                if self.KartyGracza[0][i] == '0':
                    self.KartyGracza[0][i] = ' '
                    self.KartyGracza[1][i] = ' '
                    
            os.system( 'cls' )#czyszczenie Termianala (działa w konsoli windows)
            
            print(" Karty Krupiera: ", end="")
            for i in range(0,10):
                print(f'{self.KartyKrupiera[0][i]} {self.KartyKrupiera[1][i]}  ', end="")

            print("\n\n Karty Gracza: ", end="")
            for i in range(0,10):
                print(f'{self.KartyGracza[0][i]} {self.KartyGracza[1][i]}  ', end="")
            

            if self.WartoscGracza > 0:
                print("\n\n Wartość kart Krupiera: {}".format(self.WartoscKrupiera))
                print(" Wartość kart Gracza: {}".format(self.WartoscGracza))
            print("\n Twój zakład: ", self.zaklad ,"Twoje środki: ", int(self.kasa))
    
            for i in range(0,10):   #Pętla do wrzucenia zpowrotem "0" w pustych miejscach " ", w celach do liczenia ilości kart
                if self.KartyKrupiera[0][i] == ' ' :
                    self.KartyKrupiera[0][i] = '0'
                    self.KartyKrupiera[1][i] = '0'

                if self.KartyGracza[0][i] == ' ':
                    self.KartyGracza[0][i] = '0'
                    self.KartyGracza[1][i] = '0'

        
        if self.start == True:     #Pierwsze rozdanie (1 karta krupiera zakryta)
            os.system( 'cls' )#czyszczenie Termianala (działa w konsoli windows)
            print(" Karty Krupiera: ",f'{self.KartyKrupiera[0][0]} {self.KartyKrupiera[1][0]}',"[ X ]")                        
            print("\n Karty Gracza:   ",f'{self.KartyGracza[0][0]} {self.KartyGracza[1][0]}  {self.KartyGracza[0][1]} {self.KartyGracza[1][1]}')
            if self.WartoscGracza > 0:
                print("\n Wartość kart Krupiera: X")
                print(" Wartość kart Gracza: {}".format(self.WartoscGracza))
            print("\n Twój zakład: ", self.zaklad ,"Twoje środki: ", int(self.kasa))
            self.start = False

    def wartoscKartKrupiera(self):
        self.WartoscKrupiera = 0
        self.liczAkrupiera = 0
        for i in range(0,10):   #Ta część sumuje wartość wszystkich kart
            self.WartoscKrupiera = self.WartoscKrupiera + int(self.wartosciKart[self.KartyKrupiera[0][i]])
    
            if self.KartyKrupiera[0][i] == "A": #zliczam ile asów ma krupier
                self.liczAkrupiera =+ 1
                
        #Poniższa pętla ustawia dostosowuje wartosci asów krupiera na na 1 jeśli wartość kart jest > niż 21
        if self.WartoscKrupiera > 21 and self.liczAkrupiera > 0:     #Jeśli karty krupiera mają więcej niż 21 i ma on asa lub asy to wtedy zredukuj te asy...
            for i in range(0,self.liczAkrupiera):                  #Liczba iteracji = liczbie asów
                if self.WartoscKrupiera > 21:                     #Jeśli nadal wartość kart > 21
                    self.WartoscKrupiera = self.WartoscKrupiera - 10 #...to zredukuj jednego asa do wartosci 1.        

    def wartoscKartGracza(self):
        self.WartoscGracza = 0
        self.liczAgracza = 0
        for i in range(0,10):   #Ta część sumuje wartość wszystkich kart
            self.WartoscGracza =  self.WartoscGracza + int(self.wartosciKart[self.KartyGracza[0][i]])           #Wartosc kart gracza
            
            if self.KartyGracza[0][i] == "A":   #zliczam ile asów ma gracz
                self.liczAgracza =+ 1
                
        #Poniższa pętla ustawia dostosowuje wartosci asów gracza na 1 jeśli wartość kart jest > niż 21
        if self.WartoscGracza > 21 and self.liczAgracza > 0:     #Jeśli karty gracza mają więcej niż 21 i ma on asa lub asy to wtedy zredukuj te asy...
            for i in range(0,self.liczAgracza):                  #Liczba iteracji = liczbie asów
                if self.WartoscGracza > 21:                     #Jeśli nadal wartość kart > 21
                    self.WartoscGracza = self.WartoscGracza - 10 #...to zredukuj jednego asa do wartosci 1.

    def licznikKart(self):  #liczy ilość kart krupier i gracza
        self.LiczKartGracza = 10 - self.KartyGracza[0].count('0')     #Liczę ile jest kart w rece na podstawie ilości "0" w liście.
        self.LiczKartKrupiera  = 10 - self.KartyKrupiera[0].count('0') #Liczę ile jest kart w rece na podstawie ilości "0" w liście.
        self.liczPobranychKart = self.LiczKartGracza + self.LiczKartKrupiera

    def SprwadzWynik(self): #Sprawdza i nalicza wygrane / przegrane
        if 21 >= self.WartoscGracza > self.WartoscKrupiera and self.ruchGracza != "h":  # Po hicie tych warunków nie sprawdzaj
        #win
            if 21 == self.WartoscGracza:
                print("\n BlackJack!\n Brawo! Wygrałeś ",self.zaklad,"!")   #blackjack
                self.wynik = "Wygrana"
                self.kasa = int(self.kasa) + int(self.zaklad)*2
                #print('Print 1')
                
            else:
                print("\n Brawo! Wygrałeś!",self.zaklad,"!")
                self.wynik = "Wygrana"
                self.kasa = int(self.kasa) + int(self.zaklad)*2
                #print('Print 2')
                 
        if 21 >= self.WartoscKrupiera > self.WartoscGracza and self.ruchGracza != "h":  # Po hicie tych warunków nie sprawdzaj
        #loose
            print("\n Niestety, przegrałeś ",self.zaklad)
            self.wynik = "Przegrana"
            #print('Print 3')
            
        if 21 < self.WartoscGracza:
        #loose
            print("\n Niestety, przegrałeś ",self.zaklad)
            self.wynik = "Przegrana"
            #print('Print 4')
            
        if 21 < self.WartoscKrupiera and self.ruchGracza != "h":            # Po hicie tych warunków nie sprawdzaj
        #win
            if 21 == self.WartoscGracza:    #blackjack
                print("\n BlackJack!\n Brawo! Wygrałeś ",self.zaklad,"!")
                self.wynik = "Wygrana"
                self.kasa = int(self.kasa) + int(self.zaklad)*2
            else:
                print("\n Brawo! Wygrałeś ", self.zaklad,"!")
                self.wynik = "Wygrana"
                self.kasa = int(self.kasa) + int(self.zaklad)*2
                #print('Print 5')
            
        if self.WartoscKrupiera == self.WartoscGracza and self.ruchGracza != "h":       # Po hicie tych warunków nie sprawdzaj
        #remis
            print("\n Remis!")
            self.wynik = "Remis"
            self.kasa = int(self.kasa) + int(self.zaklad)
            #print('Print 6')

        if self.wynik == "Przegrana" and int(self.kasa) <= 0:   #Jeśli gracz przegrał i ma puste konto
            decyzja = input(" Masz puste konto... jesli chcesz zagrac jeszcze raz \n nacisnij 't', lub 'z' aby zakonczyc:")
            if decyzja == 'z':
                self.zakoncz()  

        if self.wynik == "Remis" or self.wynik == "Przegrana" or self.wynik == "Wygrana":   #Jeśli gracz wygrał lub przegrał lub zremisował to zpytaj czy gra dalej czy wyłącza grę.
            if int(self.kasa) > 0:
                decyzja = input(" Nacisnij 'Enter' aby kontynuować, lub literkę 'z' aby skończyć grę:")
                if decyzja == 'z':
                    self.zakoncz()
            

    def zakoncz(self):
        print (" Do zobaczenia wkrótce! Zamykam się...")
        for i in range(0,3):
            time.sleep(1)
            print(".")
        os.sys.exit(1)
        
        
            

#Wątek główny        
talia = Talia()
talia.potasuj(talia.TaliaPotasowana)
stol = Stol(talia.TaliaPotasowana)   
stol.Start()

###Główna pętla:
while True:

    stol.RuchGracza()
    if stol.nastGra == True:
        time.sleep(2)
        talia.potasuj(talia.TaliaPotasowana)
        stol.Talia = talia.TaliaPotasowana
        stol.Start()
    
    #print("Dziala czyszczenie!")
    #break

    
