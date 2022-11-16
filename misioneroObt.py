import Model.Arbol as ar
import Model.Orilla as ori

def checkEstado(estadoAct, estadoHis):
    if (estadoAct[0].getNMisioneros() == 3) \
            or (estadoAct[0].getNMisioneros() == estadoAct[0].getNCanibal()) \
            or (estadoAct[0].getNMisioneros() == 0):
        if estadoAct not in estadoHis:
            return True
    return False

def guardar():
    estadoAct = [orIzq, posicion]
    if checkEstado(estadoAct, estadoHis):
        nodos.append(ar.Arbol(nodo, [ori.Orilla(orIzq.getNCanibal(), orIzq.getNMisioneros()), posicion]))
        nodosHijos.append(ar.Arbol(nodo, [ori.Orilla(orIzq.getNCanibal(), orIzq.getNMisioneros()), posicion]))
    orIzq.nCanibal = canibales
    orIzq.nMisioneros = misioneros

nodo = ar.Arbol(None, [ori.Orilla(3, 3), True])
nodos = [nodo]
estadoHis = []
orIzq = ori.Orilla(3, 3)

while (nodo.getEstado()[0].getNMisioneros() + nodo.getEstado()[0].getNCanibal() != 0) and len(nodos) > 0:

    nodosHijos = []
    barca = nodos[0].getEstado()[1]
    misioneros = nodos[0].getEstado()[0].getNMisioneros()
    canibales = nodos[0].getEstado()[0].getNCanibal()
    orIzq.setNCanibal(nodos[0].getEstado()[0].getNCanibal())
    orIzq.setNMisioneros(nodos[0].getEstado()[0].getNMisioneros())

    if barca:
        posicion = False
        # Misionero
        if misioneros >= 2:
            orIzq.llevarMisionero(2)
            guardar()
        # Canibal
        if canibales >= 2:
            orIzq.llevarCanibal(2)
            guardar()
        # Ambos
        if canibales >= 1 and misioneros >= 1:
            orIzq.llevarAmbos()
            guardar()

    else:
        posicion = True
        # Misionero
        if misioneros < 2:
            orIzq.traerMisionero(2)
            guardar()
        if misioneros < 3:
            orIzq.traerMisionero(1)
            guardar()
        # Canibal
        if canibales < 2:
            orIzq.traerCanibal(2)
            guardar()
        if canibales < 3:
            orIzq.traerCanibal(1)
            guardar()
        # Ambos
        if canibales < 3 and misioneros < 3:
            orIzq.traerAmbos()
            guardar()
    estadoHis.append([ori.Orilla(orIzq.getNCanibal(), orIzq.getNMisioneros()), barca])
    nodos.pop(0)
    nodo.setHijos(nodosHijos)
    nodo = nodos[0]

nodo.mostrarOrilla()
