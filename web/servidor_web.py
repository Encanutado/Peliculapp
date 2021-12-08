from flask import Flask, request, redirect, url_for, session
from flask import render_template
from web.servicios import autenticacionweb
from Servicios.Autenticación import Autenticacion

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autenticacionweb.validar_credenciales(request.form['login'], request.form['password']):
            error = 'Credenciales inválidas'
        else:
            user_id = Autenticacion.login(request.form['login'], request.form['password'])
            user_id = user_id[0]['IDUSUARIO']
            user = Autenticacion.get_user_by_id(user_id)
            user_data = {'IDUSUARIO': user_id, 'NAME': user[0][1], 'CORREO': user[0][2], 'REALNAME': user[0][3], 'LASTNAME': user[0][4]}
            session['user_data'] = user_data
            print('tamos probando el user id manito', user_id)
            return redirect(url_for('inicio'))
    return render_template('login.html', error=error)


@app.route('/list', methods=['GET', 'POST'])
def list_users():
    userslist = autenticacionweb.obtener_usuarios()
    return render_template('list_users.html', userslist=userslist)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        if not autenticacionweb.crear_usuario(request.form['login'], request.form['password'], request.form['Correo'],
                                              request.form['realname'], request.form['lastname']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('inicio'))
    return render_template('registro.html', error=error)


@app.route('/inicio')
def inicio():
    session_data = None
    logged = False
    if 'user_data' in session:
        session_data = session['user_data']
        logged = True
    return render_template('inicio.html', data=session_data, logged=logged)


@app.route('/profile')
def profile():
    session_data = None
    logged = False
    if 'user_data' in session:
        session_data = session['user_data']
        logged = True
    return render_template('profile.html', data=session_data, logged=logged)


@app.route('/delete', methods=['POST', 'GET'])
def delete_user():
    if 'user_data' in session:
        user_id = session['user_data']['IDUSUARIO']
        autenticacionweb.delete_user(user_id)
        session.pop('user_data', None)
        return redirect('login')




@app.route('/modify_user', methods=['POST', 'GET'])
def update_user():
    if 'user_data' in session:
        user_id = session['user_data']['IDUSUARIO']
        data = {'CORREO': request.form['editEmail'], 'NAME': request.form['editUserName'],
                'REALNAME': request.form['editName'], 'LASTNAME': request.form['editLastname']}
        if autenticacionweb.modify_user(user_id, data):
            return redirect('inicio')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('user_data', None)
    return redirect(url_for('login'))



app.secret_key = 'uiashsfiahfjaojfopaFASfaisjfiaop123ñ'
if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
