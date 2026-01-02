from IPython.display import display
import pandas as pd
import numpy as np
from clases.abiertos import Abiertos

def busqueda_A_estrella(problema, traza=False):
    """
    Implementación de la búsqueda A* siguiendo el pseudocódigo proporcionado.
    Devuelve el nodo solucion, o None si no se encuentra.
    """
    EA = None
    SUC = []
    debugData =[]
    columns = ["Actual","Abiertos","Sucesores", "Cerrados"]
    n0 = problema.inicial
    n0.setF(n0.getG()+n0.getH())
    ABIERTOS = Abiertos()
    ABIERTOS.put(n0)
    CERRADOS = {}

    while ABIERTOS:
        EA = ABIERTOS.pop()[1]
        if problema.es_objetivo(EA):
            if traza:
                    debugData.append([str(EA),str(list(map(lambda x:x,ABIERTOS.getQueue()))),str(SUC),str(list(map(lambda x:str(x),CERRADOS)))])
                    display(pd.DataFrame(np.array(debugData), columns=columns))
            return EA
        
        SUC = problema.sucesores(EA)
        for suc in SUC:
            suc.setF(suc.getG()+suc.getH())

        debugData.append([str(EA),str(list(map(lambda x:str(x),ABIERTOS.getQueue()))),str(SUC),str(list(map(lambda x:str(CERRADOS[x]),CERRADOS)))])

        CERRADOS[EA.getEstado()]=EA


        for suc in SUC:
                        
            nodoAb = ABIERTOS.getNodo(suc.getEstado())

            nodoCer=None
            if suc.getEstado() in CERRADOS:
                nodoCer=CERRADOS[suc.getEstado()] 

            if nodoCer is None and nodoAb is None:
                ABIERTOS.put(suc)
                
            else:
                if nodoCer is None:
                    if nodoAb.getF()>suc.getF():
                        ABIERTOS.update(nodoAb,suc)
                else:
                    #quiere decir que estaba en cerrados
                    if nodoCer.getF()>suc.getF():
                        ABIERTOS.put(suc)
                        CERRADOS.pop(suc.getEstado())


    display(pd.DataFrame(np.array(debugData), columns=columns))
    return None