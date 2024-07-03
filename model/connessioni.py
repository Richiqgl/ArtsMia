from dataclasses import dataclass
from model.artobject import ArtObject
@dataclass
class Connesione:
    v1:ArtObject
    v2:ArtObject
    Peso:int

    def __str__(self):
        return f"Arco {self.v1.object_id} - {self.v2.object_id} - peso:{self.Peso}"