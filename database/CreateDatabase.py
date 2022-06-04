import mysql.connector

db = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "root")
myCursor = db.cursor()

def CreateDatabase():
    myCursor.execute("CREATE DATABASE LoadBalancerDB")
