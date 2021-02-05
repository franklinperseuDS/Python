#Faça um programa que leia um número inteiro e mostre na tela a sua tabuada.
#obs fiz com um loop por preguiça de digitar 11 vezes


print("="*10,"Exercicio 9", "="*10)

numero = int(input("Digite um número: "))

i = 0

while i < 11:
    print(f'{numero} x {i:2} = {numero*i:2}')
    i= i+1