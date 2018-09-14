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

#def add_cart(id,name,inf):
    #cursor.execute("INSERT INTO `mybd`.`cart` (`id`, `name`, `inf`) VALUES ('"+str(id)+"', '"+str(name)+"', 'ортопед', 101, '8.00-12.00', 'Ортопедическая')")

