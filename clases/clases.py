import queue as queue

class Nodo:
    def __init__(self,estado,padre,g, h=None):
        "Inicializamos cada uno de los atributos que componen la clase Nodo"
        self.estado=estado
        self.padre=padre
        self.g = g
        if h is None:
            self.h=0
        else:
            self.h = h
        "Por defecto, f toma el valor de g"
        self.f = g

    "Creamos los getter de cada uno de los atributos"
    def getPadre(self):
        return self.padre
    def getEstado(self):
        return self.estado
    def getG(self):
        return self.g
    def getH(self):
        return self.h
    def getF(self):
        return self.f
    
    "Creamos el setter de f"
    def setF(self,f):
        self.f=f
        
    "Esta funcion crea una lista de nodos desde el actual hasta el inicio"
    def camino(self):
        x = self
        result =  []
        while x:
            result.append(x.getEstado())
            x = x.getPadre()
        return list(reversed(result))
    
    "Metodo __repr__ para listas y diccionarios"
    def __repr__(self):
        return "Nodo "+str(self.estado)+"(f:"+str(self.f)+" g:"+str(self.g)+" h:"+str(self.h)+")"
    
    "Metodo __repr__ para listas y diccionarios"
    def __str__(self):
        return "Nodo "+str(self.estado)+"(f:"+str(self.f)+" g:"+str(self.g)+" h:"+str(self.h)+")"

    "Metodo __eq__ para dicccionarios"
    def __eq__(self, other):
        return self.getEstado()==other.getEstado()
    
    "Metodo __lt__ para dicccionarios"
    def __lt__(self, other):
        return self.f<other.f
    

    

class Abiertos():
    def __init__(self):
        self.colaPrioridad = queue.PriorityQueue()
    
    def put(self,nodo):
        self.colaPrioridad.put((nodo.getF(),nodo))
    
    def pop(self):
        return self.colaPrioridad.get()
    
    def empty(self):
        return self.colaPrioridad.empty();
    
    def getNodo(self,estado):
        for elem in self.colaPrioridad.queue:
            if elem[1].getEstado()==estado:
                return elem[1]
        return None           
    
    def update(self,nodoViejo,nodoNuevo):
        self.colaPrioridad.queue.remove((nodoViejo.getF(),nodoViejo))
        self.colaPrioridad.put((nodoNuevo.getF(),nodoNuevo))

    def remove(self,nodo):
        self.colaPrioridad.queue.remove((nodo.getF(),nodo))
        
    def getNodes(self):
        return list(map(lambda x:x[1],self.colaPrioridad.queue))
    
    def getQueue(self):
        return self.colaPrioridad.queue
    
    def __str__(self):
        return str(self.colaPrioridad.queue)
        
        

class Problema:
    def __init__(self, inicial, objetivos=None):
        """
        inicial: nodo desde el que se inicia la búsqueda.
        objetivos: nodo o conjunto de nodos objetivo.
        """
        self.inicial = inicial
        self.objetivos = objetivos

    def acciones(self, nodo):
        """
        Debe devolver una lista de acciones disponibles desde el nodo dado.
        Este método debe ser implementado en una subclase concreta.
        """
        raise NotImplementedError("Método acciones no implementado")

    def resultado(self, nodo, accion):
        """
        Debe devolver el nuevo nodo que resulta de aplicar la acción al nodo dado.
        """
        raise NotImplementedError("Método resultado no implementado")

    def test_objetivo(self, nodo):
        """
        Verifica si el nodo dado es uno de los objetivos.
        """
        if isinstance(self.objetivos, list) or isinstance(self.objetivos, set):
            return nodo in self.objetivos
        else:
            return nodo == self.objetivos

    def coste(self, nodo, accion):
        """
        Devuelve el coste de aplicar una acción en un estado dado.
        Para búsqueda en anchura, por defecto es 1.
        """
        return 1

