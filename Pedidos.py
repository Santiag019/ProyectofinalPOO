from db import db

class Pedidos(db.Model):
    
    __tablename__="pedido"
    
    id=db.Column(db.Integer,primary_key=True)
    
    Contenido=db.Column(db.String(100))
    Nenvio=db.Column(db.String(10))
    Peso=db.Column(db.String(10))
    direccion=db.Column(db.String(10))
    valor=db.Column(db.String(70))
    telefono=db.Column(db.String(15))
    propietario=db.Column(db.String(70))
    observaciones=db.Column(db.String(500))
    
    def __init__(self,contenido,Nenvio,peso,direccion,valor,telefono,propietario,observaciones):
        
        self.Contenido=contenido
        self.Nenvio=Nenvio
        self.peso=peso
        self.direccion=direccion
        self.valor=valor
        self.telefono=telefono
        self.propietario=propietario
        self.observaciones=observaciones
    
    