#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('='*10,'Exercicio 15','='*10)
quilometro = float(input('Digite a quantidade de Kms pecorridos pelo carro: '))
dias = int(input('Digite a quantidade de dias que o cliente ficou com o carro: '))

pagar = (quilometro * 0.15) + (60*dias)

print(f'O cliente deve pagar R${pagar}')
