from Datos.database import BaseDeDatos


def create_movie(idPelicula, Nombre, Descripcion, Elenco, Restriccionedad, Fecha, Calificacion, Poster):
    create_movie_sql = f"""
        INSERT INTO PELICULAS(idPelicula, Nombre, Descripcion, Elenco, Restriccionedad, Fecha, Calificacion, Poster)
        VALUES ({idPelicula},'{Nombre}','{Descripcion}','{Elenco}','{Restriccionedad}','{Fecha}','{Calificacion}','{Poster}')
    """
    database = BaseDeDatos()
    database.ejecutar_sql(create_movie_sql)


def delete_movie(idPelicula):
    delete_movie_sql = f"""
    DELETE FROM PELICULAS WHERE idPelicula = {idPelicula}
"""
    database = BaseDeDatos()
    database.ejecutar_sql(delete_movie_sql)


def get_movie(idPelicula):
    get_movies_sql = f""" SELECT IDPELICULA, NOMBRE FROM PELICULAS WHERE idPelicula = {idPelicula}"""
    database = BaseDeDatos()
    selected_movie = database.ejecutar_sql(get_movies_sql)
    return selected_movie


def get_all_movies():
    get_all_movies_sql = f""" SELECT * FROM PELICULAS"""
    database = BaseDeDatos()
    movies_list = database.ejecutar_sql(get_all_movies_sql)
    return movies_list
