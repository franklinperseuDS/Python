# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros


print("="*10,"Exercicio 8", "="*10)

tamanho = float(input('Digite uma distância em metros: '))

cm = tamanho * 100
mm = tamanho * 1000

print(f"É equivalente a {cm:.2f}cm e a {mm:.2f}mm ")