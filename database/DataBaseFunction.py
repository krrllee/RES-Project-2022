import mysql.connector

db = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "root", database = "LoadBalancerDB")
myCursor = db.cursor()

def ubaci(value, code, date, dataset):
    myCursor.execute(f"INSERT INTO {dataset} (value, code, date) VALUES ({value}, {code}, {date})")
    db.commit()

def ispisi(dataset):
    myCursor.execute(f"SELECT * FROM {dataset}")
    for i in myCursor:
        print(i)