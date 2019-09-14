def rozbij_na_cyfry(liczba):
    cyfry_liczby = list(str(liczba))
    #cyfry_liczby_int = []
    #for i in range(0, len(cyfry_liczby)):
    #    cyfry_liczby_int.append(int(cyfry_liczby[i],10))
    print(cyfry_liczby)
    return cyfry_liczby





def policz_litery():
    liczba_liter = {1: 3, 2:3, 3:5,4:4, 5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:7,19:8,20:6,30:6, 40:5, 50:5, 60:5, 70: 7, 80: 6, 90:6, 100:7, 1000:8}

    #tysiac {}=
    suma_liter = 0
    for i in range(1,1000+1): #petla iterujaca po podanym zakresie liczb

        cyfry_liczby = rozbij_na_cyfry(i)
        Lcyfr = len(cyfry_liczby) #ilosc cyfr


            #print("Liczba cyfr",Lcyfr, n)
            #Tu chciałem łączyć poszczególne liczby w całość i je liczyć. jesli nie znajdzie liczby w słowniku

        suma_liter = licz_liczby(i, cyfry_liczby, Lcyfr)

        if Lcyfr == 1:
            suma_liter = suma_liter + liczba_liter[i]#one two three
        if Lcyfr == 2:
            if i < 20:
                suma_liter = suma_liter + liczba_liter[i] # eleven, fifteen etc
            if i > 19:
                if int(cyfry_liczby[1]) == 0:
                    suma_liter = suma_liter + liczba_liter[i] # twenty, therty, forthy
                else:
                    #print(i, cyfry_liczby,int(cyfry_liczby[0]+"0"),int(cyfry_liczby[1]))
                    suma_liter = suma_liter + liczba_liter[int(cyfry_liczby[0]+"0")] + liczba_liter[int(cyfry_liczby[1])] #twenty three

        if Lcyfr == 3:
            dziesietna = int(cyfry_liczby[1]+cyfry_liczby[2]) #część dziesiętna
            if dziesietna == 0:
                suma_liter = suma_liter + liczba_liter[int(cyfry_liczby[0])] + liczba_liter[100]
                continue
            if dziesietna < 20:
                suma_liter = suma_liter + liczba_liter[int(cyfry_liczby[0])] + liczba_liter[100] + len("and") + liczba_liter[dziesietna] #three hundred eleven +and(3)
            if dziesietna > 19:
                if int(cyfry_liczby[2]) == 0: #gdy część dziesiętna jest wielokrotnością liczby dziesięć
                    suma_liter = suma_liter + liczba_liter[int(cyfry_liczby[0])] + liczba_liter[100] + len("and") + liczba_liter[dziesietna] #three hundred twenty
                else: #gdy część jedności jest niezerowa
                    suma_liter = suma_liter + liczba_liter[int(cyfry_liczby[0])] + liczba_liter[100] + liczba_liter[int(cyfry_liczby[1]+"0")] + len("and") + liczba_liter[int(cyfry_liczby[2])] #three hundred twenty two


        if i == 1000: #dodanie tysiąca
            suma_liter = suma_liter + liczba_liter[1000] + len("one")



    print(suma_liter)
    return True

def policz_litery2():
    liczba_liter = {1: 3, 2:3, 3:5,4:4, 5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:7,19:8,20:6,30:6, 40:5, 50:5, 60:5, 70: 7, 80: 6, 90:6, 100:7, 1000:8}

    #tysiac {}=
    suma_liter = 0
    for i in range(1,1000+1): #petla iterujaca po podanym zakresie liczb

        cyfry_liczby = rozbij_na_cyfry(i)
        Lcyfr = len(cyfry_liczby) #ilosc cyfr
        if int(cyfry_liczby[0]) == 0 and int(cyfry_liczby[1]) == 0:
            pass




    return True

if __name__ == "__main__":
    policz_litery()
