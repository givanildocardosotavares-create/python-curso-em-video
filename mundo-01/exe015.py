'''Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.'''

dias_alugado = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias_alugado * 60) + (km * 0.15)
print(f'O valor total a pagar é R${pago:.2f}')
