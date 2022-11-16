class Arbol:
    def __init__(self,padre, estado):
        self.padre = padre
        self.estado = estado
        self.hijos = []


    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getPadre(self):
        return self.padre

    def setPadre(self, padre):
        self.padre = padre

    def getHijos(self):
        return self.hijos

    def setHijos(self, hijos):
        self.hijos = hijos

    def mostrar(self):
        print(f"\nN hijos: {len(self.getHijos())}")

        print(f"{self.estado}")

        if (self.padre != None):
            # print(f"{self.estado} y mi padre es {self.padre.estado}")
            self.padre.mostrar()
        # else:
            # print(f"{self.estado}")


    def mostrarOrilla(self):
        if (self.padre != None):
            self.padre.mostrarOrilla()

        print(f"\nN hijos: {len(self.getHijos())}")
        print(f"Canibales: {self.estado[0].nCanibal}\nMisioneros: {self.estado[0].nMisioneros}\nBarca:{self.estado[1]}")