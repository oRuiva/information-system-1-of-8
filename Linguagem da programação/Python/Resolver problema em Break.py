# Crie um programa que receba um número
#natural n(n>1) e exiba uma mensagem indicando
#se n é primo ou não.

n = int(input('Digite um número: '))
divisor = 2

while divisor < n:
    print(f'{n} % {divisor} = {n % divisor}')
    if n % divisor == 0:
        break
    divisor += 1

if divisor == n:
    print('Primo')
else:
    print('Não primo')
