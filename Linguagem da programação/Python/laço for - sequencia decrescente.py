# Crie um programa que solicite ao usuário um número
#natural e exiba a sequência decrescente do número dado
#até 1.

n = int(input('número: '))
for i in range(n, 0, -1): #leitura sempre da esquerda pra direita, ('onde começa', 'onde quero chegar',
    print(i, end= ' ')    #  'quantos em quantos numeros')
