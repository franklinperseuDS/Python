"""
Faça um programa que leia 3 numeros e fale qual é o maior e qual é o menor
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if ( num1 > num2 and num1 > num3):
    print(f"Maior numero é {num1}")
elif ( num2 > num1 and num2 >num3):
    print(f'Maior numero é {num2}')
else:
    print(f'Maior número é {num3}')

if ( num1 < num2 and num1 < num3):
    print(f"Menor numero é {num1}")
elif ( num2 < num1 and num2 <num3):
    print(f'Menor numero é {num2}')
else:
    print(f'Menor número é {num3}')