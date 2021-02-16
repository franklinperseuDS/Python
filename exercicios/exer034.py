"""
Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento

para salarios superiores a R$ 1.250,00 . Calcule um aumento de 10%

para inferiores ou iguais é de 15%
"""

print('Calculo de Salário')

salario = float(input("Digite o Valor do Salário do Colaborador: "))

if (salario > 1250):
    salario = salario * 1.10
else:
    salario = salario * 1.15

print(f"O novo salário do Colaborador é : R$ {salario:.2f}")