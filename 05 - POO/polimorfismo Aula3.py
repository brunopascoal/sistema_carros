class Animal:
    def emitir_som(self):
        print("Som..")


class Cachorro(Animal):

    def emitir_som(self):
        print("Au Au")


class Gato(Animal):

    def emitir_som(self):
        print("Miau")


gato = Gato()
gato.emitir_som()
