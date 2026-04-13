#Dados diversos números inteiros, exibir a média
#dos números lidos. A entrada termina com a leitura
#do número -1 que não deve ser contabilizado.

soma = 0
qtd = 0
n = int(input('Digite um numero inteiro: '))

while n != -1:
    soma += n
    qtd += 1
    n = int(input('Digite um numero inteiro: '))
print(f'Média {soma/qtd}')

