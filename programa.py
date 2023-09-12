from flask import Flask
from flask import render_template, request, redirect, session
from flaskext.mysql import MySQL
import hashlib
from CRUD import Crud

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'db4free.net'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'usuario_adso02'
app.config['MYSQL_DATABASE_PASSWORD'] = 'S3n4+2023'
app.config['MYSQL_DATABASE_DB'] = 'instituto_03'
mysql.init_app(app)

conexion = mysql.connect()
cursor = conexion.cursor()

Elcrud = Crud(mysql)



@app.route('/')
def inicio():

    resultado = Elcrud.leer()

    return render_template('index.html', leer = resultado)


@app.route('/crear', methods=['post'])
def crear():

    Id_aula = request.form['aula']
    descripcion = request.form['descripcion']
    capacidad = request.form['capacidad']
    id_edificio = request.form['edificio']
    audiovisual = request.form['audiovisual']
    usuario = request.form['usuario']

    Elcrud.crear([Id_aula, descripcion, capacidad, id_edificio, audiovisual, usuario])

    return redirect('/')


@app.route('/borrar/<aula>', methods=['post'])
def borrar(aula):

    Elcrud.eliminar(aula)

    return redirect('/')


@app.route('/actualizar/<aula>', methods=['GET'])
def actualizar(aula):

    actualizar_aulas = Elcrud.ver_actualizar(aula)

    return render_template('actualizar.html', actualizar = actualizar_aulas[0])


@app.route('/actualizar/datos', methods=['post'])
def actualizar_datos():
    id = request.form['aula']
    descripcion = request.form['descripcion']
    capacidad = request.form['capacidad']
    id_edificio = request.form['edificio']
    audiovisual = request.form['audiovisual']
    usuario = request.form['usuario']

    # Agregar instrucciones de impresión para verificar los valores
    print("ID:", id)
    print("Descripcion:", descripcion)
    print("Capacidad:", capacidad)
    print("ID Edificio:", id_edificio)
    print("Audiovisual:", audiovisual)
    print("Usuario:", usuario)

    # Añadir instrucciones de registro para la consulta SQL
    sql = f"UPDATE aulas SET descripcion = '{descripcion}', capacidad = {capacidad}, idEdificio = '{id_edificio}', equipoAudiovisual = {audiovisual}, usuario = '{usuario}' WHERE idAula = '{id}'"
    print("SQL Query:", sql)

    try:
        Elcrud.actualizar_datos([id, descripcion, capacidad, id_edificio, audiovisual, usuario])
        # Agregar un registro para verificar que se haya ejecutado la actualización correctamente
        print("Actualización de datos exitosa")
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir durante la actualización
        print("Error durante la actualización:", str(e))

    return redirect('/')











if __name__ == '__main__':
    app.run(debug=True)