#wymiary siatki:
xs=20
ys=xs
#aktualna wsp. znacznika
x=xs
y=ys

w = xs+1    #tworzenie listy dwuwymiarowej
h = ys+1
siatka = [[0 for x in range(w)] for y in range(h)]  #pierwsza jest wsp y druga jest x

siatka[xs][ys]=0        #zawsze ostatni element = 0
for n in range(0, ys):  #wpisuje 1 tam gdzie jest tylko 1 wariant sciezki czyli na granicach
    siatka[n][xs]=1

for n in range(0, xs):  #wpisuje 1 tam gdzie jest tylko 1 wariant sciezki czyli na granicach
    siatka[ys][n]=1


for iks in range(xs,-1,-1):     #iteracja po iksach
    #print(iks)
    for igrek in range(ys, -1, -1):     #iteracja po igrekach
        if iks==igrek==xs:
            siatka[igrek][iks]=0    #nadmiarowa petla, ale pozwala pominac prawy dolny rog
            continue

        #print (igrek)
        if iks < xs and igrek < ys:  #liczenie sciezek ale nie na obrzezach, serce algorytmu
            siatka[igrek][iks]=siatka[igrek][iks+1] + siatka[igrek+1][iks]

for n in range(0,ys+1):     #drukowanie siatki
    print(siatka[n][::])
