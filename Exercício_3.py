#Crie um programa capaz de mostrar a sequencia de Fibonacci até o n-ésimo termo desejado. 
# Exemplo para n=6 a saída deverá ser: 1,1,2,3,5,8
termos = int(input("Quantidade de números:"))

n1 = 0
n2 = 1
print('{},{}'.format(n1,n2), end='')
cont = 3
while cont <= termos:
    n3 = n1 + n2
    print(',{}'.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1