#Crie um programa capaz de calcular a função matemática "fatorial". 
# Se possível resolva utilizando recursividade
def fatorial(num):
    if num == 1:
        return 1
    return num * fatorial(num - 1)
