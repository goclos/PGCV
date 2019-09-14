import numbers
zbior = 100#zbior
nty = 0
fib = [0]*zbior  #tworzenie tablicy o wilekości zbioru
suma_paz=2
#zaczynajac od 1...

fib[0]=1
fib[1]=2
#Petla for zaczynajac od i=2,czyli element nr 3 w ciagu fiboneciego
for i in range(2, zbior):
    fib[i]=fib[i-1]+fib[i-2]
    #paz=fib[i] / 2 #sprawdzanie pazystosci
    if fib[i]>4000000:
        break
    is_even = (fib[i] & 1)
        
    if is_even==0:
        suma_paz=suma_paz+fib[i]
        #print (fib[i])





print (fib)
print (suma_paz)

    
