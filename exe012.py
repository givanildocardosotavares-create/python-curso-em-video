#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
p = float(input('Digite o valor do produto? R$ '))
d = p * 0.95
print(f'O valor do produto é R${p} reais, com 5% de desconto ficará R${d:.2f} reais.')