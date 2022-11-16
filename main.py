# This is a sample Python script.
import Model.Arbol as ar
import Model.Orilla as ori

def checkEstado(estadoAct, estadoHis):
    if (estadoAct[0][0] >= estadoAct[0][1]) or (estadoAct[0][0] == 0):
        if (estadoAct[1][0] >= estadoAct[1][1]) or (estadoAct[1][0] == 0):
            if estadoAct not in estadoHis:
                return True
    return False

orIzq = ori.Orilla(3,3)
orDer = ori.Orilla(0,0)
nodo = ar.Arbol(None,[[3,3],[0,0],True])
nodos = [nodo]
estadoHis = []

while(nodo.getEstado()[1][0] + nodo.getEstado()[1][1] != 6) and len(nodos) > 0:


    nodosHijos = []
    barca = nodos[0].getEstado()[2]
    orillaIzquierdaM = nodos[0].getEstado()[0][0]
    orillaDerechaM = nodos[0].getEstado()[1][0]
    orillaIzquierdaC = nodos[0].getEstado()[0][1]
    orillaDerechaC = nodos[0].getEstado()[1][1]
    estadoActIzq = [nodos[0].getEstado()[0][0], nodos[0].getEstado()[0][1]]
    estadoActDer = [nodos[0].getEstado()[1][0], nodos[0].getEstado()[1][1]]


    if barca:
        # Misionero
        if orillaIzquierdaM >= 2:
            estadoActIzq[0] -= 2
            estadoActDer[0] += 2
            if checkEstado([estadoActIzq,estadoActDer,False], estadoHis):
                nodos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,False]))
                nodosHijos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,False]))
        estadoActIzq = [orillaIzquierdaM, orillaIzquierdaC]
        estadoActDer = [orillaDerechaM, orillaDerechaC]

        # Canibal
        if orillaIzquierdaC >= 2:
            estadoActIzq[1] -= 2
            estadoActDer[1] += 2
            if checkEstado([estadoActIzq,estadoActDer,False], estadoHis):
                nodos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,False]))
                nodosHijos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,False]))
        estadoActIzq = [orillaIzquierdaM, orillaIzquierdaC]
        estadoActDer = [orillaDerechaM, orillaDerechaC]

        # Misionero Canibal
        if orillaIzquierdaM >= 1 and orillaIzquierdaC >= 1:
            estadoActIzq[0] -= 1
            estadoActIzq[1] -= 1
            estadoActDer[0] += 1
            estadoActDer[1] += 1
            if checkEstado([estadoActIzq,estadoActDer,False], estadoHis):
                nodos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,False]))
                nodosHijos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,False]))
        estadoActIzq = [orillaIzquierdaM, orillaIzquierdaC]
        estadoActDer = [orillaDerechaM, orillaDerechaC]
    else:
        # Misionero
        if orillaDerechaM >= 1:
            estadoActDer[0] -= 1
            estadoActIzq[0] += 1
            if checkEstado([estadoActIzq,estadoActDer,True], estadoHis):
                nodos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,True]))
                nodosHijos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,True]))
        estadoActIzq = [orillaIzquierdaM, orillaIzquierdaC]
        estadoActDer = [orillaDerechaM, orillaDerechaC]

        if orillaDerechaM >= 2:
            estadoActDer[0] -= 2
            estadoActIzq[0] += 2
            if checkEstado([estadoActIzq,estadoActDer,True], estadoHis):
                nodos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,True]))
                nodosHijos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,True]))
        estadoActIzq = [orillaIzquierdaM, orillaIzquierdaC]
        estadoActDer = [orillaDerechaM, orillaDerechaC]

        # Canibal
        if orillaDerechaC >= 1:
            estadoActDer[1] -= 1
            estadoActIzq[1] += 1
            if checkEstado([estadoActIzq,estadoActDer,True], estadoHis):
                nodos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,True]))
                nodosHijos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,True]))
        estadoActIzq = [orillaIzquierdaM, orillaIzquierdaC]
        estadoActDer = [orillaDerechaM, orillaDerechaC]

        if orillaDerechaC >= 2:
            estadoActDer[1] -= 2
            estadoActIzq[1] += 2
            if checkEstado([estadoActIzq,estadoActDer,True], estadoHis):
                nodos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,True]))
                nodosHijos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,True]))
        estadoActIzq = [orillaIzquierdaM, orillaIzquierdaC]
        estadoActDer = [orillaDerechaM, orillaDerechaC]

        # Misionero Canibal
        if orillaDerechaC >= 1 and orillaDerechaM >= 1:
            estadoActDer[1] -= 1
            estadoActIzq[1] += 1
            estadoActDer[0] -= 1
            estadoActIzq[0] += 1
            if checkEstado([estadoActIzq,estadoActDer,True], estadoHis):
                nodos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,True]))
                nodosHijos.append(ar.Arbol(nodo, [estadoActIzq,estadoActDer,True]))
        estadoActIzq = [orillaIzquierdaM, orillaIzquierdaC]
        estadoActDer = [orillaDerechaM, orillaDerechaC]
    estadoHis.append([[orillaIzquierdaM, orillaIzquierdaC], [orillaDerechaM, orillaDerechaC],barca])
    nodos.pop(0)
    nodo.setHijos(nodosHijos)
    nodo = nodos[0]

nodo.mostrar()