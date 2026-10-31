'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.'''

from math import trunc

numero = float(input('Digite um valor: '))
print(f'O número digitado foi {numero} e sua porção inteira é {trunc(numero)}.')

# Assunto: módulo math (trunc)
# trunc(x) corta a parte decimal sem arredondar (3.7 -> 3 | -3.7 -> -3)