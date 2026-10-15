#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Dolar 5.19
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.13
euro = real / 5.96
print(f'Com R${real:.2f} você pode comprar €{euro:.2f} euros.')
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f} dólares.')