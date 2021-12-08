from Datos.database import BaseDeDatos

'''CRUD de Usuarios.'''

def create_user(name, pw, Correo, realname, lastname ):
    create_user_sql = f"""
        INSERT INTO USUARIOS(name, pw, Correo, REALNAME, LASTNAME)
        VALUES ('{name}','{pw}','{Correo}', '{realname}', '{lastname}')
    """
    database = BaseDeDatos()
    database.ejecutar_sql(create_user_sql)

def get_all_users():
    get_all_users_sql = f""" SELECT * FROM USUARIOS"""
    database = BaseDeDatos()
    listausuarios = database.ejecutar_sql(get_all_users_sql)
    return listausuarios


def crear_sesion(id_usuario, dt_string):
    print('creosesion')
    crear_sesion_sql = f"""
               INSERT INTO SESIONES(ID_USUARIO, FECHA_HORA)
               VALUES ('{id_usuario}', '{dt_string}')
           """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_sql)


def obtener_sesion(id_sesion):
    print('se obtuvo sesion.')
    obtener_sesion_sql = f"""
        SELECT ID, ID_USUARIO, FECHA_HORA FROM SESIONES WHERE ID = {id_sesion}
    """
    bd = BaseDeDatos()
    return [{"id": registro[0],
             "id_usuario": registro[1],             "fecha_hora": registro[2]}
            for registro in bd.ejecutar_sql(obtener_sesion_sql)]


def get_user_by_nameAndPw(nombre, clave):
    obtener_usuario_sql = f"""
            SELECT IDUSUARIO, NAME, PW 
            FROM USUARIOS u
            WHERE NAME='{nombre}' and PW='{clave}'
        """
    bd = BaseDeDatos()
    return [{"IDUSUARIO": registro[0],
             "NAME": registro[1],
             "PW": registro[2]
             } for registro in bd.ejecutar_sql(obtener_usuario_sql)]


def get_user_by_id(id):
    obtener_usuario_sql = f"""
            SELECT IDUSUARIO, NAME, CORREO, REALNAME, LASTNAME
            FROM USUARIOS u
            WHERE IDUSUARIO= {id}
        """
    bd = BaseDeDatos()
    ejecucion = bd.ejecutar_sql(obtener_usuario_sql)
    return ejecucion

def delete_user(id):
    delete_user_sql = f"""DELETE FROM USUARIOS WHERE IDUSUARIO = {id}"""
    bd = BaseDeDatos()
    bd.ejecutar_sql(delete_user_sql)


def update_user(user_id, data):
    update_sql = f"""
            UPDATE USUARIOS
            SET CORREO = '{data['CORREO']}', NAME = '{data['NAME']}' ,REALNAME = '{data['REALNAME']}', 
            LASTNAME = '{data['LASTNAME']}'  
            WHERE IDUSUARIO = {user_id};
            """
    bd = BaseDeDatos()
    bd.ejecutar_sql(update_sql)