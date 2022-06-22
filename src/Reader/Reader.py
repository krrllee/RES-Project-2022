from Worker import DBFunctions

class Reader:

    def run(self):
        while True:
            print("Unesi komandu:\n1.Pretraga po kodu\n2.Pretraga po intervalu\n")

            try:
                komanda = int(input())
                if(komanda == 1):
                    self.pretragaPoKodu()
                if(komanda == 2):
                    self.pretragaPoIntervalu()
                else:
                    print("Nepostojeca komanda.")
            except:
                exit()
                


    def pretragaPoKodu(self):
        db = DBFunctions()
        print("Unesi kod: ")
        code = str(input())
        if((code != "CODE_ANALOG") and (code != "CODE_DIGITAL") and (code !="CODE_CUSTOM") and (code != "CODE_LIMITSET") and (code != "CODE_SINGLENOE") and (code !="CODE_MULTIPLENODE")and(code!="CODE_CONSUMER")and(code!="CODE_SOURCE")):
            print("Nepostojeci kod.")

        dataset = self.getDataSet(code)

        retVal = db.getDataFromCode(code,dataset)

        return retVal

    def getDataSet(self,code):
        if(code == "CODE_ANALOG")or(code == "CODE_DIGITAL"):
            dataset = 1
        elif(code == "CODE_CUSTOM")or(code == "CODE_LIMITSET"):
            dataset = 2
        elif(code == "CODE_SINGLENODE")or(code == "CODE_MILITPLENOD"):
            dataset = 3
        elif(code == "CODE_CONSUMER")or(code == "CODE_SOURCE"):
            dataset = 4
        return dataset


    def pretragaPoIntervalu(self):
        db = DBFunctions()
        print("Unesi kod: ")
        code = str(input())

        if((code != "CODE_ANALOG") and (code != "CODE_DIGITAL") and (code !="CODE_CUSTOM") and (code != "CODE_LIMITSET") and (code != "CODE_SINGLENOE") and (code !="CODE_MULTIPLENODE")and(code!="CODE_CONSUMER")and(code!="CODE_SOURCE")):
            print("Nepostojeci kod.")
            
        dataset = self.getDataSet(code)
            
        print("Unesi pocetni interval: ")
        firstTimestamp = str(input())

        print("Unesi krajnji interval: ")
        secondTimestamp = str(input())

        retVal = db.getDataFromTimestamp(firstTimestamp,secondTimestamp,dataset)
        return retVal

        

            


