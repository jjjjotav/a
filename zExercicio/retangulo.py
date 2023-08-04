from forma import forma
    
class retangulo(forma):
    def __init__(self):
        super().__init__()
        self.base = 0.0
        self.altura = 0.0

    def AreaRetangulo(self):
        return self.base * self.altura
    

    def __str__(self):
        return f'base: {self.base}\naltura: {self.altura}'
    
    
