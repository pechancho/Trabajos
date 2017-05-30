
class Instrumento():
    def  __init__(self,tipo):
        self.tipo = tipo
    def sonar():
        print "sonando", tipo
    def afinar():
        print "afino"
class Guitarra(Instrumento):
    def __init__(self,tipo,cuerda):
        Instrumento.__init__(self,tipo)
        self.cuerda = cuerda
    def punteo(self):
        print "esta punteado"
class Piano(Instrumento):
    def __init__(self,tipo,teclas):
        Instrumento.__init__(self,tipo)
        self.teclas = teclas
    def concierto(self):
        print " alto concierto"
class Saxo(Instrumento):
    def __init__(self,tipo,tamano):
        Instrumento.__init__(self,tipo)
        self.tamano= tamano
    def escala(self):
        print "escalado"
            
        
    
        

