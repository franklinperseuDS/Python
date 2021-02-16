'''
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando
R$ 0,50 para viagens até 200 km
e R$ 0,45 para viagens mais longas

'''

distancia = float(input("Dgite a distância da viagem em KM: "))
'''
if (distancia <= 200):
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
'''
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print(f"O preço final da sua passagem foi R${preco:.2f} \n Agradecemos a sua preferência")

