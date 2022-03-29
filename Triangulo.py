
class Triangulo:

    def __init__(self,la,lb,lc):
       self.la = la
       self.lb = lb
       self.lc = lc

    def set_la(self, la):
            self.la = la
    def set_lb(self, lb):
            self.lb = lb
    def set_lc(self, lc):
            self.lc = lc
    
    def get_la(self):
            return self.la
    def get_lb(self):
            return self.lb
    def get_lb(self):
            return self.lb

def tipo_triangulo(la,lb,lc):

    if la < lb + lc and lb < la + lc and lc < la + lb:

        if la == lb == lc:
            print("Equilátero")
        elif la != lb != lc != la:
            print("Escaleno")
        else:
                print("Isóceles")
    else:
            print("Não é um triangulo")

    