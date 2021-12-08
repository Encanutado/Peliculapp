from flask import Flask, jsonify, request
from Servicios.Autenticación import Autenticacion

app = Flask(__name__)

'''CRUD de Peliculas'''


class Movies:
    def __init__(self, idpelicula, nombre, descripcion, elenco, restriccionedad, fecha, calificacion):
        self.idpelicula = idpelicula
        self.nombre = nombre
        self.descripcion = descripcion
        self.elenco = elenco
        self.restriccionedad = restriccionedad
        self.fecha = fecha
        self.calificacion = calificacion


@app.route("/movies", methods=['GET'])
def list_movies():
    movies_list = Autenticacion.get_all_movies()
    all_movies = []
    for movie in movies_list:
        movie = {"idPelicula": movie[0], 'NOMBRE': movie[1]}
        all_movies.append(movie)
        return jsonify(all_movies)
    return "Error al cargar listado de pelicula."


@app.route("/movies/<id_search_movie>", methods=['GET'])
def get_movie(id_search_movie):
    if Autenticacion.get_movie(id_search_movie):
        movie = Autenticacion.get_movie(id_search_movie)
        movie_json = []
        print(movie)
        movie = {"idPelicula": movie[0][0], 'NOMBRE': movie[0][1]}
        movie_json.append(movie)
        return jsonify(movie_json)
    return "error master"


@app.route("/movies", methods=['POST'])
def create_movie():
    movie_data = request.get_json()
    Autenticacion.create_movie(movie_data['idPelicula'], movie_data['Nombre'], movie_data['Descripcion'],
                               movie_data['Elenco'], movie_data['Restriccionedad'], movie_data['Fecha'],
                               movie_data['Calificacion'], movie_data['Poster'])
    return "OK", 200


@app.route("/movies/<id_delete_movie>", methods=['DELETE'])
def delete_movie(id_delete_movie):
    Autenticacion.delete_movie(id_delete_movie)
    return "OK", 200




'''CRUD para Usuarios'''

@app.route('/users', methods=['POST'])
def crear_usuario():
    user_data = request.get_json()
    if 'name' not in user_data:
        return "Username is required.", 412
    if 'pw' not in user_data:
        return "Password is required.", 412
    if 'Correo' not in user_data:
        return "Email required"
    if 'realname' not in user_data:
        return 'Name Required'
    if 'lastname' not in user_data:
        return 'lastname requires'
    Autenticacion.create_user(user_data['name'], user_data['pw'], user_data['Correo'], user_data['realname'], user_data['lastname'])
    return 'OK', 200

@app.route('/users', methods=['GET'])
def list_users():
    users_list = Autenticacion.get_all_users()
    all_users = []
    for users in users_list:
        users = {'IDUSUARIO': users[0], 'NAME': users[1], 'Correo': users[3], 'REALNAME': users[4], 'LASTNAME': users[5]}
        all_users.append(users)
    return jsonify(all_users)


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    Autenticacion.delete_user(id)


@app.route('/modify_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    for date in data:
        if date not in data or data[f'{date}'] == '':
            return f"El dato '{date}' es requerido."
    print('Esta es la data pa', data)
    Autenticacion.update_user(user_id, data)
    return 'Se ha actualizado su usuario.', 200



'''Endpoint para el login.'''

@app.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    datos_usuario = request.get_json()
    print(datos_usuario)
    if 'nombre' not in datos_usuario:
        return 'El nombre de usuario es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    #id_sesion = Autenticacion.login(datos_usuario['nombre'], datos_usuario['clave'])
    usuario_logueado = Autenticacion.login(datos_usuario['nombre'], datos_usuario['clave'])
    print('este man se logueo', usuario_logueado)
    return jsonify({"user_id": usuario_logueado[0]})



if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
