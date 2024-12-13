import psycopg2


#################################################
#################################################
#################################################
#################################################

connection1 = psycopg2.connect(
host="localhost",
user="postgres",
password="Mariano302",
database="registro_usuarios",
port="5432"
)
# autocommit
connection1.autocommit = True

#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################

connection2 = psycopg2.connect(
host="localhost",
user="postgres",
password="Mariano302",
database="minimarketdb",
port="5432"
)
# autocommit
connection2.autocommit = True

#################################################
#################################################
#################################################
#################################################

def traer_todos_losdatos_proveedores():
    cursor= connection1.cursor()
    query_data = f"SELECT nombre_proveedor, telefono FROM proveedores ORDER BY id_proveedor"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()
    return data

def registrar_usuario(account, username, password):
    pass

def existe_usuario(username):
    cursor= connection1.cursor()
    query_data = f"SELECT nombre FROM usuarios WHERE nombre = '{username}'"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()

    if data == []:
        return True
    else: 
        return False


def verificar_contrasenia(password, username, account):
    cursor= connection1.cursor()
    query_data2 = f"SELECT usuarios.id_usuario, contrasenas.contrasena, usuarios.admin FROM usuarios JOIN contrasenas ON usuarios.id_usuario = contrasenas.id_usuario WHERE usuarios.nombre = '{username}'"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()
    ##################ORDENAR PARA CORREGIR QUE VERIFIQUE SI ES USUARIO O ADMIN 

    if account == "Administrador":
        account = True
    else:
        account = False     #Aacomoda la variable account a un true o fals epara verificar que tipo de cuenta es

    if data != []:
        if data[0][1] != password or data[0][2] != account: ## verifica password igual y si el tipo es igual al seleccionado
            return True # devuelve true si alguno es distinto para tirar el mensaje de error
    else:
        return False

