import mysql.connector


def getConexao():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mudar789!',
        database='SINASC'
    )
    return con
