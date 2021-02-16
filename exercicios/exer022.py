'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiusculas
- o nome com todas minusculas
- quantas letras ao todo(sem considerar espaço)
- quantas letras tem o primeiro nome

'''

nome = input('Digite seu nome completo: ').strip()

print(nome.upper())

print(nome.lower())

print(f'Tamanho do nome: {len(nome) - nome.count(" ")}')

nome = nome.split()

primeiro = nome[0]
print(f'Tamanho do primeiro nome:{len(primeiro)}')

'''outra solução para encontrar o primeiro nome é
  nome.find(' ') ao inves de splitar
'''