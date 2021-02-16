'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem
ou não formar um triângulo

extra info : Não é necessário fazer as três somas para verificar a possibilidade de um triângulo existir.
 Basta fazer a soma entre os dois lados menores. Se a soma entre eles for maior que o terceiro lado, então,
 a soma entre qualquer um deles e o terceiro lado (que é o maior) terá o mesmo resultado.
'''

r1 = float(input("Digite o valor da primeira reta :"))
r2 = float(input("Digite o valor da segunda reta :"))
r3 = float(input("Digite o valor da terceira reta :"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+r2:
     print("os Seguimentos formam um Triângulo")
else:
        print("Os seguimentos não formam um Triângulo")
