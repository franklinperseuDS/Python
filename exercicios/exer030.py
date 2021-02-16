'''
Crie um número inteiro qualquer e mostre se é impar ou par.

'''

numero = int(input("Digite um numero para ver se é par ou impar: "))

if (numero % 2 == 0):
    print(f"o Número {numero} é PAR")
else:
    print(f"o Número {numero} é IMPAR")