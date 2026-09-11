#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
algo = input('Digite algo: ')
print(f'o tipo primitvo desse valor é {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabeto? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúscula? {algo.isupper()}')
print(f'Está em minúscula? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')

