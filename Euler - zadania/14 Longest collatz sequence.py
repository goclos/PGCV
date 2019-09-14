licznik=1
tymcz=0
maxLicz=0
maxFirst=0
#n=13
#print (n)
for n in range(50, 900000):
    tymcz=n
    while n!=1:         #wykonuje dopóki n jest rozne niz 1
        
        if n%2==0:      #n jest pazyste
            n=n/2
            #print (n)
            licznik=licznik+1
        

        else:           #n jest niepazyste
            n=(3*n)+1
            #print (n)
            licznik=licznik+1

    #print (tymcz, licznik)
    if licznik>maxLicz:
        maxLicz=licznik
        maxFirst=tymcz
    licznik=1
    

print (maxFirst, maxLicz)


