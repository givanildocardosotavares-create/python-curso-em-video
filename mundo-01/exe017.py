''' Faça um progrma que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''

from math import hypot

# Solicita ao usuário os comprimentos dos catetos

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Calcula o comprimento da hipotenusa usando o teorema de Pitágoras

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

# Exibe o resultado

print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")