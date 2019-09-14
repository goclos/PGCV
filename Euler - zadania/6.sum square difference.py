#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
zbior=101
sumak=0
kwadrats=0



#suma kwadratow
for i in range(1,zbior):
    sumak=sumak+(i*i)
    print(i, sumak)



#kwadrat sumy
for n in range(1,zbior):
    kwadrats=kwadrats+n
kwadrats=kwadrats*kwadrats

roznica=kwadrats-sumak

print(sumak)
print(kwadrats)
print(roznica)
