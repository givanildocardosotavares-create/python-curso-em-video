#Faça um programa que leia a largura e a altura de uma parede em metros,calcule sua área e a quantidade de tinta necessára para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area:.2f}m².')
tinta = (area / 2)
print(f'Para pintar esta parede, você precisará de {tinta}l de tinta.')

