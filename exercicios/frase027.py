'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

ex: Ana maria de Souza

primeiro = ANA
ultimo = Souza
'''


nome = input("Digite seu nome: ")
nome = nome.split()

print(f'Primeiro: {nome[0]} ')
#print(len(nome))
print(f'Ultimo: {nome[len(nome)-1]}')