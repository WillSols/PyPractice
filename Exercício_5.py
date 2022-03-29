#Crie um programa capaz de calcular a função matemática "fatorial". 
# Se possível resolva utilizando laços de repetição
n = int(input('Numero para fatoração:'))
x = n
f = 1
while x > 0:
    f = f * x
    x -= 1

print ( ' O fatorial é {}'.format(f))