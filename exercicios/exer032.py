"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
informações adicionais
    Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
    Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
    Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
    O ano é bissexto (tem 366 dias).
    O ano não é um ano bissexto (tem 365 dias).

    400 – bissexto 500 – não bissexto 600 – não bissexto 800 – bissexto 1200 – bissexto 1500 – bissexto 1700 – não bissexto 1800 – não bissexto 1900 – não bissexto 2000 – bissexto
     2100 – não bissexto 2200 – não bissexto 2300 – não bissexto 2400 bissexto
Teste de software
#ano = [1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052]
#ano = [400, 500, 600, 800, 1200, 1500, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400]
"""
from datetime import date
ano = int(input('Digite um ano para saber se é bissexto:\nColoque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano %100 != 0 or ano % 400 == 0):
    print(f"o Ano  {ano} é Bissexto!")
else:
    print(f"O ano {ano} Não é Bissexto!")