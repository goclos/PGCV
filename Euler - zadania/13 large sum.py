# Creates a list containing 5 lists, each of 8 items, all set to 0
import numpy as np
suma=0
k=20
w=20
tab = [[0] * k] * w
file=open("13wsad.txt", "r")
tresc=file.read()
file.close()
posrednia=tresc.split()#przejscie ze stringa na tablice stringow

for i in range(0,len(posrednia)):#petla przechodzoca na tablice INT
    posrednia[i]=int(str(posrednia[i]))#tablica jednowymiarowa intow

#print (posrednia[99])


for i in range(0,len(posrednia)):
    suma=suma+posrednia[i]
    print(i)

print (suma)    
