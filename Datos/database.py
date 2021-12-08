import sqlite3
import os.path


class BaseDeDatos:
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    url_base_de_datos = os.path.join(SITE_ROOT, "Tablas/", "peliapp.db")

    def _crear_conexion(self):
        try:
            self.conexion = sqlite3.connect(BaseDeDatos.url_base_de_datos)
        except Exception as e:
            print(e)

    def _cerrar_conexion(self):
        self.conexion.close()
        self.conexion = None

    def ejecutar_sql(self, sql):
        self._crear_conexion()
        cur = self.conexion.cursor()
        cur.execute(sql)

        filas = cur.fetchall()

        self.conexion.commit()
        self._cerrar_conexion()

        return filas
