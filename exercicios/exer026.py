'''

Crie um programa que leia uma frase e mostre
- quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- em que posição ela aparece a ultima vez.

'''
frase = input("Digite uma frase qualquer: ")

frase = frase.upper().strip()

print(f'Aparecem {frase.count("A")} A')

p = frase.find('A')
u = frase.rfind('A')

print(f'Posição do primeiro a {p+1}')
print(f'Posição do ultimo a {u+1}')