#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

print("="*10,"Exercicio 12", "="*10)

valor = float(input('Digite o valor do produto: '))

desconto = valor * 0.95

print(f'O novo preço do produto é ${desconto:.2f}')