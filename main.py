from flask import Flask, render_template, request, redirect, url_for, flash,make_response
from connect import connectionBD
from flask import redirect
from psycopg2.extras import DictCursor
import sqlite3
import logging
import psycopg2


app = Flask(__name__)

@app.route('/contactanos', methods=['GET', 'POST'])
def registrarForm():
    
    # Esto es el manejo del formulario
    msg = ''
    try:
        if request.method == 'POST':
            nombredecontacto = request.form.get('nombredecontacto', '')
            calle = request.form.get('calle', '')
            ciudad = request.form.get('ciudad', '')
            postcode = request.form.get('postcode', '') 
            telefono = request.form.get('telefono', '')
            email = request.form.get('email', '')
            mensaje = request.form.get('mensaje', '')
            
            # Para conectarme a la base de datos
            conexionbd = connectionBD()
            if conexionbd:
                cursor = conexionbd.cursor(cursor_factory=DictCursor)
            
            # Inserccion en la base de datos
                sql = "INSERT INTO contactanos (nombredecontacto, calle, ciudad, postcode, telefono, email, mensaje) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                valores = (nombredecontacto, calle, ciudad, postcode, telefono, email, mensaje)
                cursor.execute(sql, valores)
                conexionbd.commit()
                
                # cerrando bd
                cursor.close()
                conexionbd.close()
                print(cursor.rowcount, "Registro insertado")
                print("1 registro insertado, id", cursor.lastrowid)
                
                msg = 'Registro exitoso'
                
                return render_template('contactanos.html', msg='formulario enviado')
            else:
                msg = 'No se pudo establecer la conexión con la base de datos.'
                
    # Manejo de Excepciones:
    except Exception as e:
        msg = f'Error: {repr(e)}'
    # Respuesta de Error:
    return render_template('contactanos.html', msg=f'Error en el formulario: {msg}')

@app.route('/formulario-enviado',  methods=['GET'])
def formulario_enviado():
    return render_template('formulario-enviado.html')


# @app.route('/contactanos', methods=['GET', 'POST'])
# def contactanos():
#     print(request.form)  # Agrega esta línea para imprimir los datos del formulario

#     try:
#         if request.method == 'POST':
#             # Procesar los datos del formulario y almacenarlos en la base de datos
#             nombredecontacto = request.form['nombredecontacto']
#             calle = request.form['calle']
#             ciudad = request.form['ciudad']
#             postocode = request.form['postocode']
#             telefono = request.form['telefono']
#             email = request.form['email']
#             mensaje = request.form['mensaje']
#             nda = request.form.get('nda', False)

#             # Conectar a la base de datos (en este ejemplo, SQLite)
#             conn = sqlite3.connect('mi_basededatos.db')
#             cursor = conn.cursor()

#             # Crear y ejecutar la consulta SQL
#             consulta = "INSERT INTO contactanos (nombredecontacto, calle, ciudad, postocode, telefono, email, mensaje, nda) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
#             cursor.execute(consulta, (nombredecontacto, calle, ciudad, postocode, telefono, email, mensaje, nda))
#             conn.commit()  # Confirmar
#             conn.close()  # Cerrar la conexión

#             # Establecer el mensaje de confirmación

#     except Exception as e:
#         app.logger.error('Error al insertar en la base de datos: %s', repr(e))
#         flash('Hubo un problema al procesar tu solicitud. Por favor, inténtalo de nuevo más tarde.', 'error')

#     # Renderizar la plantilla con el mensaje de confirmación
#     return render_template('contactanos.html')


@app.route('/inicio', methods=['GET'])
def inicio():
    return render_template('inicio.html')


@app.route('/blog', methods=['GET'])
def blog():
    return render_template('blog.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

