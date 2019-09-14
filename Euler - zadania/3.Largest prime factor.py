dzielna=600851475143
liczba=10000
dzielnik=2
znacznik=0
index=0
pierwsze=[0]*liczba
czynniki=[0]*100 #czynniki pierwsze


for k in range(2,liczba):#petla przeszukujaca wszytkich liczba pierwszych w zakresie
    for u in range(1,k):#petla sprawdzajaca pojedyncza liczbe
        res=k % u
        if res == 0:
            znacznik=znacznik+1
            
    if znacznik < 2:
        #print(k)
        pierwsze[index]=k
        index=index+1
        znacznik=0
    znacznik=0

#print(pierwsze)





###Trzeba zmienić sposób generowania liczba pierwszych


#liczba pierwsza to taka która dzieli się tylko przez siebie oraz przez 1

#w kżdym kroku dzielimy przez najmniejszą możliwie liczbę,
#jesli zostaje reszta to znaczy że trzeba spróbować innej wartości(+1) i spróbować jeszcze raz
#i tak dalej rozbijając na coraz mniejsze liczby

k=0 #index w liscie liczb pierwszych
f=0 #index w liscie czynnikow pierwszych
m=0 #marker szukania
while m == 0:
    reszta=dzielna%pierwsze[k]
    print(dzielna, pierwsze[k])
    if reszta !=0:
        #oznacza to że dzielnik był  za maly!
        k=k+1
    if reszta == 0:
        #print(f,k,) 
        czynniki[f]=pierwsze[k] #jesli nie ma reszty z dzielenia mod to znaczy ze jest czynnik pierwszy
        if dzielna == pierwsze[k] or dzielna<=1: #jesli
            m=1
            #print(dzielna, pierwsze[k])
            break
        dzielna=dzielna/pierwsze[k]
        f=f+1 #zwieksz index w tablicy czynnikow pierwszych
        k=k+1 #zwieksz index w tablicy liczb pierwszych
        reszta=1
    
    
        
            
        

print(czynniki)
suma=1
for n in range (0, len(czynniki)):
    if czynniki[n]==0:
        break
    suma=suma*czynniki[n]

print(suma)


    
        
