def empurra(v,n):
    i=0
    while i<n-1:
        while v[i]>v[i+1]:
            troca(v,i,i+1)
        i += 1

def troca(v,i,j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp

def exibe(v,n):
    i=0
    while i<n:
        print(v[i], end='')
        i += 1
    '\n'


v = ([40,20,50,30,10])
n = 5
exibe(v,n)
tam = n
while tam>1:
    empurra(v,tam)
    exibe(v,tam)
    tam -= 1
exibe(v,n)