from Triangulo import Triangulo
from Triangulo import tipo_triangulo

triangulos = []

id = 1

flag = False

while True:
    print('Insira as medidas')

    id = int(+1)
    la = float(input("Lado A:"))
    lb = float(input("Lado B:"))
    lc = float(input("Lado C:"))

    f = Triangulo('','','')
    f.set_la(la)
    f.set_lb(lb)
    f.set_lc(lc)

    triangulos.append(f)

    tipo_triangulo(la,lb,lc)