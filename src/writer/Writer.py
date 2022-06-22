import socket
import pickle
import time
import random



class Writer:
    

    def __init__(self,adresa):
        self.adresa = adresa
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def start(self):
        while(True):
            print("1 - Slanje podataka\n2 - Paljenje Worker komponente\n3 - Gasenje Worker komponente\n",end ="")
            
            try:
               komanda = int(input())
               poruka = ""
               if(komanda == 1):
                   poruka = self.uzmiPodatke()
               elif(komanda == 2):
                    poruka = "UPALI:0"
               elif(komanda == 3):
                    poruka = "UGASI:0"
               else:
                   print("Nepostojeca komanda.")
                   

               if(poruka !=""):
                   self.s.connect(self.adresa)
                   poruka = poruka.encode()
                   self.s.send(poruka)
                   time.sleep(2)
                   print("Poruka poslata.")
                   
            except ValueError:
                print("Morate uneti broj!")
            except Exception as e:
                print("Konekcija nije uspostavljena.")
                print(e)
        self.s.close()

                   

    def uzmiPodatke(self):

        mess = ""
        print("Unesi kod (moguci kodovi za unos: CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE) : ",end="")
        code = input()

        #PROVJERI DA LI JE UNETI KOD ODGOVARAJUCI ONIMA IZ LISTE
        if((code != "CODE_ANALOG") and (code != "CODE_DIGITAL") and (code !="CODE_CUSTOM") and (code != "CODE_LIMITSET") and (code != "CODE_SINGLENOE") and (code !="CODE_MULTIPLENODE")and(code!="CODE_CONSUMER")and(code!="CODE_SOURCE")):
            print("Nepostojeci kod.")
        else:
            print("Unesi value: ")
            value = int(input())
            mess =  "Poslato:" + str(code) + ":" + str(value)
        return mess
               