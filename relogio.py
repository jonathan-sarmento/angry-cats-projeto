class Relogio:
    def __init__(self):
        self.horas = 7
        self.minutos = 0

    def __str__(self): # Pesquisar significado dessa função especifica.
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def Tempogasto(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
    
    def Tempofinal(self):
        return (self.horas > 9 or (self.horas == 9 and self.minutos > 0))