import math
import sys
#a2 + b2 = c2
#a + b + c = 1000
# a < b < c
#moje zalozenie: a, b, c > 100
a=0
b=0
c=0
potega=2
suma=1000 # suma trojki pit.
tro_mark=0
suma_mark=0
#przeszukać cały zbior?
#jak szukać?
#Pierwsszy krok: Znaleźc wszsytki trojki pitagorejskie ktorych suma jest < 100
#Drugi krok: Poszezyc zakres, ewentualnnie przesunac w okolice 1000
#3 krok: Znalezc wlasciwa trojke

for ia in range(2, 1000):
    for ib in range(2,1000):
        for ic in range(2, 1000):
            if math.pow(ia,potega)+math.pow(ib,potega)==math.pow(ic,potega):
                tro_mark=1
                print ("Trojka: ", ia,ib,ic, ia+ib+ic)
                if ia+ib+ic==suma:
                    print ("Trojka: ", ia,ib,ic)
                    print ("Suma Trojki: ", ia+ib+ic)
                    print ("Iloczyn Trojki: ",ia*ib*ic)
                    suma_mark=1
                    sys.exit()





