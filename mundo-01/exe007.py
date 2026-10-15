#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
from statistics import median
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f' A sua média foi {media:.1f}.')