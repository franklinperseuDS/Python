#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa

from math import hypot
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))

#hypo = (oposto ** 2 + adjacente **2) ** (1/2)
hypo = math.hypot(oposto,adjacente)

print(f'O comprimento da hipotenusa é {hypo:.2f}')

#3.5 # 4.75