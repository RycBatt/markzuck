print("Numeros adjacentes iguais comparator")

num = int(input("Digite seu numero meu queridao: "))
numadj = False
while num > 0:
    numant = num%10
    num = num//10
    if numant == num%10:
        numadj = True

if numadj:
    print("Existem pares iguais adjacentes! =)")
else:
    print("Não existem pares adjacentes =(")