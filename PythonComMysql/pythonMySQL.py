import mysql.connector

con = mysql.connector.connect(host='localhost', database='db_python', user='root', password='@JNL12345silva')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL")
    
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado", linha)
    
if con.is_connected():
    cursor.close()
    con.close()
    print("Acabou")