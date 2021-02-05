# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pintálo
#Sabendo que cada litro de tinta pinta uma área de 2m²
print("="*10,"Exercicio 11", "="*10)
altura = float(input('digite o valor da altura: '))
largura = float(input('digite o valor da largura: '))

area =  altura * largura



pintar = area / 2

print(f'A area da parade é {area:.2f} m² e para pintar tem que usar {pintar:.2f} L')
