class Forma:

    def area(self):
        pass


class Quadrado(Forma):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2


class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio * 2


quadrado = Quadrado(lado=4)
area_quadrado = quadrado.area()

circulo = Circulo(raio=4)
area_circulo = circulo.area()


print(f"Area do quadrado eh: {area_quadrado}")
print(f"Area do circulo eh: {area_circulo}")
