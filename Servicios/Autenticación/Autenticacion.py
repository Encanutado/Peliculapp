from Datos.Modelos import Usuario as modelosUsuario
from Datos.Modelos import Peliculas as modeloPeliculas
from datetime import datetime


def create_user(name, pw, Correo, realname, lastname):
    modelosUsuario.create_user(name, pw, Correo, realname, lastname)


def create_movie(idPelicula, Nombre, Descripcion, Elenco, Restriccionedad, Fecha, Calificacion, Poster):
    modeloPeliculas.create_movie(idPelicula, Nombre, Descripcion, Elenco, Restriccionedad, Fecha, Calificacion, Poster)


def delete_movie(idPelicula):
    modeloPeliculas.delete_movie(idPelicula)


def get_movie(idPelicula):
    movies = modeloPeliculas.get_movie(idPelicula)
    return movies


def get_all_movies():
    all_movies = modeloPeliculas.get_all_movies()
    return all_movies


def get_all_users():
    all_users = modelosUsuario.get_all_users()
    return all_users


def login(nombre, clave):
    if _existe_usuario(nombre, clave):
        usuario = modelosUsuario.get_user_by_nameAndPw(nombre, clave)
        #return _crear_sesion(usuario['IDUSUARIO'])
        return usuario
    else:
        raise Exception("El usuario no existe o la clave es invalida")


def _existe_usuario(nombre, clave):
    usuarios = modelosUsuario.get_user_by_nameAndPw(nombre, clave)
    return not len(usuarios) == 0


def _crear_sesion(id_usuario):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return modelosUsuario.crear_sesion(id_usuario, dt_string)


def validar_sesion(id_sesion):
    print('Se valido sesion.')
    sesiones = modelosUsuario.obtener_sesion(id_sesion)
    if len(sesiones) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sesiones[0]['fecha_hora'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 60:
        return False
    else:
        return True


def get_user_by_id(id):
    res = modelosUsuario.get_user_by_id(id)
    return res


def delete_user(id):
    modelosUsuario.delete_user(id)


def update_user(user_id, data):
    modelosUsuario.update_user(user_id, data)

