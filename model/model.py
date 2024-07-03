from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self._artObjectList=DAO.getAllObjects()
        self._grafo=nx.Graph()
        self._grafo.add_nodes_from(self._artObjectList)
        self._idMap={}
        for v in self._artObjectList:
            self._idMap[v.object_id]=v
    def creaGrafo(self):
        self.addEdges()

    def getConnessa(self,voInt):
        vo=self._idMap[voInt]
        #modo 1:successori di Vo
        #restituisce un dizionario
        successors=nx.dfs_successors(self._grafo,vo)
        allSucc=[]
        for v in successors.values():
            allSucc.extend(v)
        print(allSucc)
        print(f"Metodo 1 {print(len(successors.values()))}")

        # modo 2:successori di Vo
        predecessore=nx.dfs_successors(self._grafo,vo)
        print(f"Metodo 1 {print(len(predecessore.values()))}")

        #conto i nodi dall'albero di visita  metodo 3
        #restituisce un albero con un numero in piu perche conta l'origine
        tree=nx.dfs_tree(self._grafo,vo)
        print(f"metodo 3 (tree) : {len(tree.nodes)}")

        #metodo 4
        connetCamp=nx.node_connected_component(self._grafo,vo)
        print(f"metodo 4 (tree) : {len(connetCamp)}")


    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def addEdges(self):
        #self._grafo.edges.clear()

        # #soluzione1
        # for u in self._artObjectList:
        #     for v in self._artObjectList:
        #         peso=DAO.getPeso(u,v)
        #         self._grafo.add_edge(u,v,weight=peso)

        #soluzione 2
        allEdges=DAO.getAllConnessioni(self._idMap)
        for e in allEdges:
            self._grafo.add_edge(e.v1,e.v2,weight=e.Peso)
        print(len(allEdges))

    def checkExistence(self,idOggetto):
        return idOggetto in self._idMap

    def getObjFromId(self):
        pass
