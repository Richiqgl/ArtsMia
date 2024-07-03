from database.DAO import DAO
from model.model import Model
res=DAO.getAllObjects()
print(len(res))
mymodel=Model()
con=DAO.getAllConnessioni(mymodel._idMap)
print(len(con))