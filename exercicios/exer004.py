#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
print("==========Exercicio 4 ==========")
n = input("Digite alguma coisa: ")

print("O tipo primitivo é: ",type(n))

print("É um alpha númerico ?", n.isalnum())
print("É um alfabético ?",n.isalpha())
print("O que foi digitado é númerico ?", n.isnumeric())
print("É um maiúsculas ?", n.isupper())
print("É um minúsculas ?", n.islower())
print("É um Título? ?", n.istitle())
print("Apenas espaços?", n.isspace())

