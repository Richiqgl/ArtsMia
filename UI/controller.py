import flet as ft
from UI.view import View

class Controller:
    def __init__(self, view:View, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Grafo contiene {self._model.getNumNodes()}"))
        self._view.txt_result.controls.append(ft.Text(f"Grafo contiene {self._model.getNumEdges()}"))
        self._view.update_page()


    def handleCompConnessa(self,e):
        idAdded=self._view._txtIdOggetto.value
        try :
            IntId=int(idAdded)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.controls.append(ft.Text("Il valore non e un numero"))
            return
        if self._model.checkExistence(IntId):
            self._view.controls.append(ft.Text(f"L'oggetto {IntId} è contenuto"))
        else:
            self._view.controls.append(ft.Text(f"L'oggetto {IntId} NON è contenuto"))

        sizeConnessa=self._model.getConnessa(IntId)
        self._view.txt_result.controls.append(ft.Text(f"La componente connesssa è {sizeConnessa}"))
        self._view.update_page()

    def handleCercaPercorso(self):
        self._model.getBestPath(int(self._view._ddLun.value),self._model.get)

        myOptNum=list()
        pass
