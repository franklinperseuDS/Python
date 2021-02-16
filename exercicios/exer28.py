'''
Escreva um programa que faça o computador 'pensar ' em um numero inteiro entre
0 e 5 e peaça para que o usuario tente descobrir qual foi o numero
escolhido pelo computador

o programa devera escrever na tela se o usuario venceu ou perdeu.
'''

from random import randint
from time import sleep

numero = randint(0,5)
print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
adv = int(input("Digite um número de 0 a 5: "))
print("Processando...")
sleep(2)
if adv == numero:
    print("Parabéns! Você conseguiu me vencer!")
else:
    print(f"Perdeu! eu pensei no número {numero}")