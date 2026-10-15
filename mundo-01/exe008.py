#Escreva um programa que leia um valor em metros e o exiba convertidos em centímetros e milímetros.
m = float(input('Informe o valor em metros: '))
cm = m * 100
mm = m * 1000
print(f'{m} metros equivale a {cm:.0f} centímetros.')
print(f'{m} metros equivale a {mm:.0f} milímetros.')
