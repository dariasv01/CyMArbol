class Orilla:
    def __init__(self, nCanibal, nMisioneros):
        self.nCanibal = nCanibal
        self.nMisioneros = nMisioneros

    def getNCanibal(self):
        return self.nCanibal

    def setNCanibal(self, nCanibal):
        self.nCanibal = nCanibal

    def getNMisioneros(self):
        return self.nMisioneros

    def setNMisioneros(self, nMisioneros):
        self.nMisioneros = nMisioneros

    def llevarCanibal(self, numero):
        result = self.getNCanibal()-numero
        if result >= 0:
            self.setNCanibal(result)

    def llevarMisionero(self, numero):
        result = self.getNMisioneros() - numero
        if result >= 0:
            self.setNMisioneros(result)

    def traerCanibal(self, numero):
        result = self.getNCanibal() + numero
        if result <= 3:
            self.setNCanibal(result)

    def traerMisionero(self, numero):
        result = self.getNMisioneros() + numero
        if result <= 3:
            self.setNMisioneros(result)

    def llevarAmbos(self):
        self.llevarMisionero(1)
        self.llevarCanibal(1)

    def traerAmbos(self):
        self.traerCanibal(1)
        self.traerMisionero(1)