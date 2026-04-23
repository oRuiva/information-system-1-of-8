soma = 0
cont = 1
numero = int(input('Digite um numero: '))

while cont <= 5:
    soma = soma + numero
    cont = cont + 1
    numero = int(input('Digite um numero: '))
print('a soma dos numeros é: ',soma)