def reverse_int(k):
    return int(str(k)[::-1])

#Zadania:
#-Jak sprawdzić czy iloczyn 2 2 cyfrowych liczb jest polindromem?
#   -mnozenie liczb, sprawdzanie czy są one polindromem, nastepna iteracja
#   
#-Jak sprawdzić największy taki polindrom? iteraca w górę

for i in range(999,100,-1):
    for n in range(999,100,-1):
        wynik=i*n
        wynik_odwrocony=reverse_int(wynik)
        #print(wynik)
        #print(wynik_odwrocony)
        if wynik==wynik_odwrocony:
            #yes!!!
            print (wynik)
            break
        
