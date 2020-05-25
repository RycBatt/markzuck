print("Numeros grandes digitos sommer")

num = int(input("Digite seu numero meu queridao: "))
soma = 0
while num > 0:
    soma = soma + num % 10
    num = num//10
print(soma)
