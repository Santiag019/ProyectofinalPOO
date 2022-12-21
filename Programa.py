from flask import Flask , render_template, request, redirect, url_for
from db import db
from Pedidos import Pedidos

class Programa:
    
    def __init__(self):
        
        self.app=Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///Pedidos.sqlite3"
        
        db.init_app(self.app)
        
        self.app.add_url_rule('/',view_func=self.buscarTodos)
        self.app.add_url_rule('/nuevo',view_func=self.agregar, methods=["GET","POST"])
        
        with self.app.app_context():
            db.create_all()
        
        self.app.run(debug=True)
        
    def buscarTodos(self):
        
        return render_template('mostrarTodos.html', Pedidos=Pedidos.query.all()) 
        
    def agregar(self):
        
        if request.method=="POST":
            contenido=request.form['contenido']
            Nenvio=request.form['Nenvio']
            peso=request.form['peso']
            direccion=request.form['direccion']
            valor=request.form['valor']
            telefono=request.form['telefono']
            propietario=request.form['propietario']
            observaciones=request.form['observaciones']
            
            miPedido=Pedidos(contenido,Nenvio,peso,direccion,valor,telefono,propietario,observaciones)
            
            db.session.add(miPedido)
            db.session.commit()
            
            return redirect(url_for('buscarTodos'))
            
        
        return render_template('nuevoPedido.html')
    
miPrograma=Programa()