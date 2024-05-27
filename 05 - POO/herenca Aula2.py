class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5

    def acelerar(self):
        print("Acelerando vrum vrum")

    def frear(self):
        print("Freando...")

    def buzinar(self):
        print("Bi Bi...")


class Uno(Carro):

    modelo = "Uno"
    marca = "Fiat"
    ano = "1992"


uno = Uno()
uno.buzinar()
