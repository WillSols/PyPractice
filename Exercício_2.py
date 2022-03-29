#Construa uma função que leia 3 números representando os lados de um triangulo, 
# e determine se eles formam um triangulo equilátero, isósceles ou escaleno. 
# Exemplo: Lado A=1, lado B=2, lado C=3 formam um triangulo escaleno, Lado A=1, lado B=1, lado C=2 
# formam um isósceles, Lado A=3, lado B=3, lado C=3 formam um equilátero, e Lado A=1, lado B=2, lado 
# C=5 não formam um triangulo válido

la = float(input("Lado A:"))
lb = float(input("Lado B:"))
lc = float(input("Lado C:"))


def tipo_triangulo():

    if la < lb + lc and lb < la + lc and lc < la + lb:

        if la == lb == lc:
            print("Equilátero")
        elif la != lb != lc != la:
            print("Escaleno")
        else:
            print("Isóceles")
    else:
        print("Não é um triangulo")


tipo_triangulo()