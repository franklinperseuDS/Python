#Faça um programa que leia um ânguo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

ang = float(input('Digite um angulo: '))

num = math.radians(ang)
print(f'nesse angulo {ang:.2f} temos o cosseno: {math.cos(num):.2f} , o seno {math.sin(num):.2f} e a sua tangente {math.tan(num):.2f}')
