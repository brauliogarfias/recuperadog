#PROGRAMA PRINCIPAL - CATDOG
from contextlib import nullcontext
import pymongo

import os
from flask import Flask, send_from_directory, redirect, url_for ,render_template, request
from werkzeug.utils import secure_filename
from pymongo import MongoClient

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'
#ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


cliente = MongoClient('localhost', port=27017)

db = cliente.Registro_mascota

coleccion = db.datos_mascota
coleccion = db.usuarios

#para las mascotas 
no_mascota = 0
mascotas = {}

#para los usuarios
Usuario_no = 0
usuario = {}


@app.route("/")
def home():
    return render_template("base.html")


@app.route('/agregar_mascota', methods = ['POST', 'GET'])
def agregar_mascota():
    
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        raza = request.form['raza']
        sexo = request.form['sexo']
        caracter = request.form['caracter']
        color = request.form['color']
        edad = request.form['edad']
        tamanio = request.form['tamanio']
        salud = request.form['salud']
        sociable = request.form['sociable']
        contacto = request.form['contacto']
       
        file = request.files['archivo']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        filename = 'images/' + filename

        global no_mascota
        no_mascota += 1
        id_mascota = (str(no_mascota))
        nueva_mascota = {
            "nombre" : nombre,
            "raza" : raza,
            "sexo" : sexo,
            "caracter" : caracter,
            "color" : color,
            "edad" : edad,
            "tamanio" : tamanio,
            "salud" : salud,
            "sociable" : sociable,
            "contacto" : contacto,
            "filename" : filename
            
        }

        mascotas.update({id_mascota : nueva_mascota})


        
        #datos = (nombre, raza, sexo, caracter, color, edad, tamanio, salud, sociable, contacto, filename)
        #return redirect(url_for("lista", data=datos))
        return galeria(data=mascotas)
        
        
    
    else:
        return render_template("agregar.html")



@app.route('/usuario')
def perfil():
    return render_template("Usuario.html")


@app.route('/inicio_sesion', methods = ['POST', 'GET'])
def inicio_sesion():
    
    if request.method == 'POST':

        nombreCompleto = request.form['nombreCompleto']
        generoU = request.form['generoU']
        edadU = request.form['edadU']
        telefonoU = request.form['telefonoU']
        direccionU = request.form['direccionU']
        usuario = request.form['usuario']
        contraseñaU = request.form['contraseñaU']

        global Usuario_no
        Usuario_no += 1
        id_Usuario = (str(Usuario_no))
        Nuevo_usuario = {
            "nombreU" : nombreCompleto,
            "generoU" : generoU,
            "telefonoU" : telefonoU,
            "direccionU" : direccionU,
            "usuario" : usuario,
            "edadU" : edadU,
            "contraseñaU" : contraseñaU,
        }
        
        print(Nuevo_usuario)
        

    else:
        return render_template("inicio_sesion.html")

@app.route('/seguimiento', methods = ['POST','GET'])
def seguimiento(data={}):
    return render_template("seguimiento.html", dic = data)
     

@app.route('/galeria', methods = ['POST', 'GET'])
def galeria(data={}):
    
    print(data)
    return render_template("galeria.html", dic = data)
    
    
if __name__ == '__main__':   
    app.run(debug = True) 
    


