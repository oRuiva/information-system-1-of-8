#Crie um programa para um site! O programa deverá soicitar
#o valor de um item e a quantidade de unidades compradas
#deste item, ao final, deve exibir o total com desconto de
#10%. Considere que a quantidade será um número natural positivo.

valor = float(input("valor de produto:")) #valor real do produto com pontos para centavos
qtd = int(input("Quantidade:")) #valor inteiro da quantidade
total = (valor * qtd)
desconto = total * 0.10
total_final = total - desconto
print("total com desconto: R$:", total_final) #sempre colocar virgula para ter mais de 1 argumento
