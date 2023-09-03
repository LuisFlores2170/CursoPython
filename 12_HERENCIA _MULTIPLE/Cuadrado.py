from FIguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color) -> None:
        #super().__init__(FiguraGeometrica(lado, lado))
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self) -> str:
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'