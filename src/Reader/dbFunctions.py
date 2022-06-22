from multiprocessing import connection
from pickle import TRUE
import sqlite3
from datetime import datetime

class DBFunctions:

    def dbConnect(self,dataset):
        try:
            self.connection = sqlite3.connect("database.db")
        except:
            return False
        return True
    

    def createTable(self,dataset):      
        try:
            self.connection.execute(f"""
                CREATE TABLE dataset{dataset}
                (
                    id INT PRIMARY KEY NOT NULL,
                    code TEXT NOT NULL,
                    value INT NOT NULL,
                    timestamp TEXT NOT NULL
                )
                """)
        except:
            pass

    def entityExistance(self,id,dataset):               
        retVal = self.connection.execute(f"""
            SELECT id,code,value,timestamp
            FROM dataset{dataset}
            WHERE id = {id}
            """)
        if(len(retVal.fetchall))>0:
            return True
        return False

    def updateTable(self,id,code,value,dataset):        
        timestamp = datetime.now()
        self.connection.execute(f"""
            UPDATE dataset{dataset}
            SET code = "{code}", value = {value}, timestamp = "{timestamp}"
            WHERE id = {id}
            """)
        self.connection.commit()

    def getValue(self,id,dataset):                  
        retVal = self.connection.execute(f"""
            SELECT value
            FROM dataset{dataset}
            WHERE id = {id}
            """)
        value,=retVal.fetchall()[0]
        return value

    def getDeadband(self,oldValue,newValue):            
        deadband = abs(newValue-oldValue)/ oldValue * 100
        return deadband

    def InsertIntoTable(self,id,code,value,dataset):    
        timestamp = datetime.now()
        self.connection.execute(f"""
            INSERT INTO dataset{dataset} (id,code,value,timestamp)
            VALUES ({id},'{code}',{value},'{timestamp}')
            """)
        self.connection.commit()

if __name__ == "__main__":
    db = DBFunctions()
    dataset = 2
try:
    db.dbConnect(dataset)
    x=db.updateTable(2,2,4,5)
except Exception as e:
        print(e)
else:
    print(x)
    print("Uspeo dbCONNECT")