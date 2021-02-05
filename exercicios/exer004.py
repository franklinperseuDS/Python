#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
print("==========Exercicio 4 ==========")
n = input("digite alguma coisa: ")

print(type(n))

print(n.isalnum())
print("O que foi digitado é númerico ?", n.isnumeric())
