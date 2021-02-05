#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

print("="*10,"Exercicio 7", "="*10)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

print(f"O aluno ficou com a média {media:.2f}")
