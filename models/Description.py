import enum
from http.client import _DataType
from typing import ItemsView


import Item

DataSet=(1,2,3,4)                 
#tuple mesto liste da ne bi mogle da se menjaju vrednosti
#Index krece od 0


class Description:
    def __init__(self,ID, items: list, DataSet):
        self.ID = ID
        self.items = items
        self.listaKodova = DataSet

#DataSet u opsegu od [1,4] i uzavisnosti od vrednost (1,2,3,4) u Workeru vraca 
#    1=CODE_ANALOG, CODE_DIGITAL
#    2=CODE_CUSTOM, CODE_LIMITS
#    3=CODE_SINGLENODE, CODE_MULIOPLENODE
#    4=CODE_CONSUMER, CODE_SOURCE
