import sqlite3
import os
from datetime import datetime

class DBFunctions:

   
    def dbConnect(self):
        try:
            print(os.getcwd())
            self.connection = sqlite3.connect("../Worker/database.db")
            self.cur = self.connection.cursor()
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
        try:
            retVal = self.cur.execute(f"""
            SELECT id,code,value,timestamp
            FROM dataset{dataset}
            WHERE id = {id}
            """)
            res = self.cur.fetchall()
            if(len(res)>0):
                return True
            else:
                return False       
        except Exception as e:
            print(e)
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

    def getDataFromCode(self,code,dataset):
        retVal = self.connection.execute(f"""
            SELECT id,code,value,timestamp
            FROM dataset{dataset}
            WHERE code = {code}
            """)
        return retVal.fetchall()

    def getDataFromTimestamp(self,firstTimestamp,secondTimestamp,dataset):
        retVal = self.connection.execute(f"""
            SELECT id,code,value,timestamp
            FROM dataset{dataset}
            WHERE timestamp BETWEEN '{firstTimestamp}' AND '{secondTImestamp}'
            """)
        return retVal.fetchall()
               
    def getDeadband(self,oldValue,newValue):
        deadband = abs(newValue-oldValue)/ oldValue * 100
        return deadband

    def InsertIntoTable(self,id,code,value,dataset):
        timestamp = datetime.now()
        try:
            self.cur.execute(f"""
            INSERT INTO dataset{dataset} (id,code,value,timestamp)
            VALUES ({id},'{code}',{value},'{timestamp}')
            """)
        except sqlite3.IntegrityError: 
            return 'Korisnik sa prosldjenim brojilom vec postoji'       
        self.connection.commit()
        return "Uspjesno dodato"