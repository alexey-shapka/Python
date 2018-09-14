import mysql.connector
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='mybd')

cursor = cnx.cursor()

def table(name):
    cursor.execute("SELECT * FROM "+str(name))

    row = cursor.fetchone()
    data=[]
    while row is not None:
        data.append(row)
        row = cursor.fetchone()
    return data

def add(name,password):
    cursor.execute("INSERT INTO xo (Name, Password) VALUES ('"+str(name)+"','"+str(password)+"')")
    cnx.commit()

def updatewins(name,value):
    cursor.execute("UPDATE `xo` SET `Wins`= "+str(value)+" WHERE `Name` = '"+str(name)+"';")
    cnx.commit()

def updatematches(name,value):
    cursor.execute("UPDATE `xo` SET `Matches`= "+str(value)+" WHERE `Name` = '"+str(name)+"';")
    cnx.commit()

def getwins(name):
    cursor.execute("SELECT `Wins` FROM `xo` WHERE `Name` = '"+str(name)+"'")
    row = cursor.fetchone()
    return row[0]

def getmatches(name):
    cursor.execute("SELECT `Matches` FROM `xo` WHERE `Name` = '"+str(name)+"'")
    row = cursor.fetchone()
    return row[0]

