'''
Faça um prog que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

ex:
 Digite um número : 1834

 unidade: 4
 dezena:3
 centena:8
 milhar:1
'''

numero = int(input('Digite um numero qualquer: '))


print(f' unidade: {numero //1 % 10} ')
print(f' dezena: {numero // 10 % 10} ')
print(f' centena: {numero // 100 % 10} ')
print(f' milhar: {numero // 1000 % 10} ')
