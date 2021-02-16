
frase = 'Curso em Vídeo Python'
print('frase')
print(frase)
print('imprimir uma letra')
print(frase[9])
print('fazer slice fatiar de 9 ao 12')
print(frase[9:13])
print('fazer slice fatiar de 9 ao ultimo')
print(frase[9:21])
print('fazer slice fatiar de 9 ao ultimo pulando 2 letras')
print(frase[9:21:2])
print('fazer slice fatiar de 9 ao ultimo pulando 3 letras')
print(frase[9::3])
print('fazer slice fatiar do começo ate 4')
print(frase[:5])
print('ver o tamanho da frase')
print(len(frase))
print('contar quantas letras o tem na frase')
print(frase.count("o"))
print('encontrar a posição que esta a sequencia ou character')
print(frase.find('deo'))
print('substituir na frase')
print(frase)

frase = frase.replace("Python", "Python 3")
print(frase)
print('Curso' in frase)
print(f'Colocar Maiuscula :{frase.upper()}')
print(f'Colocar Minusculo :{frase.lower()}')
print(f'Colocar  em capitalize:{frase.capitalize()}')
print(f'Colocar em formato de titulo :{frase.title()}')


print(f'dividir a string em array {frase.split()}')
frase = frase.split()
print('Juntar a string que foi separada em array')
print(frase[2][3])
print('-'.join(frase))

frase ='   aprenda python  '
print(f'Colocar tirar os espaços :{frase.strip()}')
print(f'Colocar tirar os ultimos espaços :{frase.rstrip()}')
print(f'Colocar tirar os primeiros espaços :{frase.lstrip()}')

print("""hoje estou tentando programar
é bem divertido, tem suas dificuldades
vou tentar imprimir o texto do jeito que ta usando
3 aspas juntas no print""")