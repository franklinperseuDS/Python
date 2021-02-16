"""
estilo de cores e fundos

/033[estilo;texto;fundo m
exemplo:
/033[0;33;44m


estilo cods :           text:       back
0 = none                30          40      white
1 = bold                31          41      red
4 = underline           32          42      green
7 = negative            33          43      yellow
                        34          44      blue
                        35          45      purple
                        36          46      baby blue
                        37          47      grey
"""

print (f'\033[0;33;41m Teste \033[m')

print (f'\033[4;33;44m Teste \033[m')
print (f'\033[1;35;43m Teste \033[m')
print (f'\033[30;42m Teste \033[m')
print (f'\033[m Teste \033[m')
print (f'\033[7;30m Teste \033[m')

#-------------------------------------------------------

print('\033[31m Olá Mundo! \033[m')
print('\033[0;33;44m Olá Mundo! \033[m')