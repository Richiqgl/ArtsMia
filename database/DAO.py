from database.DB_connect import DBConnect
from model.artobject import ArtObject
from model.connessioni import Connesione

class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getAllObjects():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM objects"""
        cursor.execute(query,())

        for row in cursor:
            result.append(ArtObject(**row))#se i parametri sono gli stessi di quelli della dataclass
            #posso omettere i parametri e mettere solo **row
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(v1:ArtObject,v2:ArtObject):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT COUNT(*) 
FROM exhibition_objects eo1,exhibition_objects eo2 
where eo1.exhibition_id = eo2.exhibition_id and eo1.object_id < eo2.object_id and eo1.object_id= %s and eo2.object_id=%s"""
        cursor.execute(query, (v1,v2))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getAllConnessioni(id_Map):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT  eo1.object_id as o1,eo2.object_id as o2 ,COUNT(*)as Peso
FROM exhibition_objects eo1,exhibition_objects eo2 
where eo1.exhibition_id =eo2.exhibition_id and eo1.object_id< eo2.object_id 
GROUP by eo1.object_id,eo2.object_id 
ORDER by Peso DESC """
        cursor.execute(query, ())

        for row in cursor:
            result.append(Connesione(id_Map[row["o1"]],id_Map[row["o2"]],row["Peso"]))

        cursor.close()
        conn.close()
        return result
