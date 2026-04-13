#Crie um programa que peça ao usuário preços
#de produtos comprados até que ele decida
#encerrar a compra. O programa. ao final, deve
#exibir o total gasto.

total = 0
quero_comprar = True

while quero_comprar:
    preco = float(input('preço: '))
    total += preco
    opcao = input('Quer continuar? [S/N] ')
    if opcao != 's':
        quero_comprar = False

print (f'Total a pagar: {total: .2f}')

