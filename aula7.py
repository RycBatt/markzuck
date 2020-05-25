#baskhara
import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta == 0:
    print("A função tem como raiz unica o valor ", b/2*a)
if delta > 0:
    print("A função tem como raizes os numeros {0} e {1}.".format(-b+math.sqrt(delta)/(2*a), (-b-math.sqrt(delta)/2*a)))
if delta < 0:
    print("A função não tem raizes no dominio dos reais")
