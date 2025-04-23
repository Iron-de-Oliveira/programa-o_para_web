import pymysql

def conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='15975346',
        database='banco_aluno',
        cursorclass=pymysql.cursors.DictCursor
    )

