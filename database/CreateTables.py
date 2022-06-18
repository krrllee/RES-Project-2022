import mysql.connector

db = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "root", database = "LoadBalancerDB")
myCursor = db.cursor()

def CreateTables():
    myCursor.execute("CREATE TABLE DataSet1(id int PRIMARY KEY NOT NULL AUTO_INCREMENT, code VARCHAR(50) NOT NULL, value int NOT NULL, date datetime)")
    myCursor.execute("CREATE TABLE DataSet2(id int PRIMARY KEY NOT NULL AUTO_INCREMENT, code VARCHAR(50) NOT NULL, value int NOT NULL, date datetime)")
    myCursor.execute("CREATE TABLE DataSet3(id int PRIMARY KEY NOT NULL AUTO_INCREMENT, code VARCHAR(50) NOT NULL, value int NOT NULL, date datetime)")
    myCursor.execute("CREATE TABLE DataSet4(id int PRIMARY KEY NOT NULL AUTO_INCREMENT, code VARCHAR(50) NOT NULL, value int NOT NULL, date datetime)")
