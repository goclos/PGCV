zbior = 1000 #zbior
nty = 0
wielo = [0]*zbior
dzielnikA = 3
dzielnikB = 5
suma=0
for i in range(1,zbior):
    resztaA = i % dzielnikA
    resztaB = i % dzielnikB
    if resztaA == 0 or resztaB == 0:
        wielo[nty] = i
        nty=nty+1
        suma = suma + i



print (wielo)
print (suma)
    
