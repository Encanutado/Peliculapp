import requests

from web.servicios import rest_api


def validar_credenciales(usuario, clave):
    body = {'nombre': usuario,
            'clave': clave}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    return respuesta.status_code == 200


'''CRUD Usuarios.'''

def crear_usuario(name, pw, Correo, realname, lastname):
     body = {"name": name,
             "pw": pw,
             "Correo": Correo,
             "realname": realname,
             "lastname": lastname
            }
     respuesta = requests.post(f'{rest_api.API_URL}/users', json=body)
     return respuesta.status_code == 200


def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/users')
    return respuesta.json()

def delete_user(id):
    res = requests.delete(f'{rest_api.API_URL}/delete/{id}')
    return res.status_code == 200

def modify_user(user_id, data):
    response = requests.put(f'{rest_api.API_URL}/modify_user/{user_id}', json=data)
    return response.status_code == 200

