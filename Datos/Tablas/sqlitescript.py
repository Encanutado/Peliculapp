import sqlite3



sql_tabla_usuarios='''CREATE TABLE IF NOT EXISTS USUARIOS(
                    IDUSUARIO INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT VARCHAR(50),
                    PW TEXT,
                    CORREO TEXT,
                    REALNAME TEXT VARCHAR(50),
                    LASTNAME TEXT VARCHAR(50),
                    IDPLATAFORMAS INTEGER,
                    IDROL INTEGER,
                    FOREIGN KEY(IDPLATAFORMAS) REFERENCES PLATAFORMAS(IDPLATAFORMAS),
                    FOREIGN KEY(IDROL) REFERENCES ROL(IDROL)
                    );'''

sql_tabla_rol='''CREATE TABLE IF NOT EXISTS ROL(
                IDROL INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 TIPOROL TEXT VARCHAR(20) NOT NULL
                 );'''

sql_tabla_plataformas='''CREATE TABLE IF NOT EXISTS PLATAFORMAS (
                        IDPLATAFORMAS INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        NOMBRE TEXT VARCHAR(50) NOT NULL,
                        LOGO BLOB NOT NULL,
                        DESCRIPCION TEXT NOT NULL UNIQUE
                        );'''

sql_tabla_peliculas='''CREATE TABLE IF NOT EXISTS PELICULAS
                        (IDPELICULA INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                        NOMBRE TEXT VARCHAR(50) NOT NULL,
                        DESCRIPCION TEXT VARCHAR(50) NOT NULL,
                        ELENCO TEXT,
                        RESTRICCIONEDAD INTEGER,
                        FECHA DATE,
                        CALIFICACION INTEGER NOT NULL,
                        POSTER BLOB,
                        IDCATEGORIAS INTEGER,
                        IDPLATAFORMAS INTEGER,
                        FOREIGN KEY (IDPLATAFORMAS)
                        REFERENCES PLATAFORMAS (IDPLATAFORMAS),
                        FOREIGN KEY (IDCATEGORIAS) 
                        REFERENCES CATEGORIAS (IDCATEGORIAS)
                        );'''

sql_tabla_categorias='''CREATE TABLE IF NOT EXISTS CATEGORIAS
                        (IDCATEGORIAS  INTEGER PRIMARY KEY NOT NULL,
                         DESCRIPCION TEXT VARCHAR(50) NOT NULL UNIQUE
                         );'''

sql_tabla_sesiones = '''
CREATE TABLE SESIONES(
 ID INTEGER PRIMARY KEY,
 ID_USUARIO TEXT,
 FECHA_HORA TEXT,
 FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS(IDUSUARIO) 
)
'''

if __name__ == '__main__':
    try:
        print('Crating DB')
        conexion = sqlite3.connect('peliapp.db')
        print('Creating Tables')
        conexion.execute(sql_tabla_usuarios)
        conexion.execute(sql_tabla_rol)
        conexion.execute(sql_tabla_plataformas)
        conexion.execute(sql_tabla_peliculas)
        conexion.execute(sql_tabla_categorias)
        conexion.execute(sql_tabla_sesiones)
        conexion.close()
        print('DB succesfully created.')
    except Exception as e:
        print(f'Error creating database: {e}', e)