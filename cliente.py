class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Acessando o atributo @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print('Chamando Setter nome()')
        self.__nome = nome
