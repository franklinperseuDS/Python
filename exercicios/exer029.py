"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h. mostre uma mensagem dizendo que foi multado.
a multa vai custar R$: 7,00 por cada km acima do limite

"""

velocidade = float(input("Qual a velocidade do carro: "))

if (velocidade > 80 ):
    multa = (velocidade - 80) * 7
    print(f'Você ultrapssaou o limite de 80km/h e foi multado em  R$ {multa:.2f}')

print("Parabens você é um motorista consciente")

