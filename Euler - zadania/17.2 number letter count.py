import sys
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
liczby = {0:"",1:"one",2:"two", 3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred", 1000:"thousand"}
dlugoscLiczb = liczby.copy()
for elem in dlugoscLiczb:
    #print(elem)
    dlugoscLiczb[elem] = len(dlugoscLiczb[elem])
#print(liczby)
print(dlugoscLiczb)


def liczLiczby(gornaGranica):
    sumaCalkowita=0
    for i in range(1, gornaGranica+1):
        stringLiczba = str(i)
        while len(stringLiczba) != 4:
                stringLiczba = "0"+stringLiczba


        print(stringLiczba)
        #jeśli 3 pozycja od lewej jest zerem, lub jest różna od 1 to licz jedności na podstawie pozycji 4
        if int(stringLiczba[2]) == 0 or int(stringLiczba[2]) >= 2:
            sumaCalkowita = sumaCalkowita + dlugoscLiczb[int(stringLiczba[3])]

        #Jeśli jeśli pozycja 3 jest = 1 licz nastki
        if int(stringLiczba[2]) == 1:
            sumaCalkowita = sumaCalkowita + dlugoscLiczb[int(stringLiczba[2::])]

        #Jeśli ta pozcja jest większa równa 2 to licz dziesiątki
        if  int(stringLiczba[2]) >= 2:
            sumaCalkowita = sumaCalkowita + dlugoscLiczb[int(stringLiczba[2]+"0")]


        #Licz setki
        if int(stringLiczba[1]) != 0:
            sumaCalkowita = sumaCalkowita + dlugoscLiczb[int(stringLiczba[1])] #one , two ...
            sumaCalkowita = sumaCalkowita + dlugoscLiczb[100] #hundred
            if int(stringLiczba[2:]) != 0:#jeśli setki są niezerowe to dodaj and
                sumaCalkowita = sumaCalkowita + 3 #and

        #licz tysiące
        if int(stringLiczba[0]) != 0:
            sumaCalkowita = sumaCalkowita + dlugoscLiczb[int(stringLiczba[0])] #one , two ...
            sumaCalkowita = sumaCalkowita + dlugoscLiczb[1000] #hundred



    return sumaCalkowita



#print ("This is the name of the script: ", sys.argv[0])
#print ("Number of arguments: ", len(sys.argv))
#print ("The arguments are: " , sys.argv[1])
suma = liczLiczby(int(sys.argv[1]))
print("Suma liczb od 1 do {0} to: {1}".format(sys.argv[1], suma))
