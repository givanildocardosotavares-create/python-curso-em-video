#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.
n = int(input('digite um numero: '))
m = n * 2
t = n * 3
r = n ** (1/2)
print(f'O dobro de {n} é {m}.')
print(f'O triplo de {n} é {t}.')
print(f'A raiz quadrada de {n} é {r:.2f}.')
#O 2f diz: mostre como float(f), com duas casas decimais.