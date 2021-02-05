# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros


print("="*10,"Exercicio 8", "="*10)

tamanho = float(input('Digite um número a ser convertido: '))

cm = tamanho * 100
mm = tamanho * 1000

print(f"É equivalente a {cm}cm e a {mm}mm ")