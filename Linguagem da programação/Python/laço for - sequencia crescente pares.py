# Crie um programa que solicite ao usuário
#um número natural e exiba a sequência de 0
#até o número dado, somente pares.

n = int(input('número: '))
for i in range (0, n+1, 2):
    print(i, end= ' ')