valor = float(input('Preço unitário: '))
qtd = int(input('Quantidade comprada: '))

total = valor * qtd

if qtd >=25 or total>200:
    desconto = 0.08 * total
    total -= desconto

print(f'Valor final: R$ {total: .2f}')
