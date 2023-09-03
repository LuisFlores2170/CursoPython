from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto) -> None:
        
        self._ancho = ancho if self._valid(ancho) else 0
        self._alto = alto if  self._valid(alto) else 0

    @property
    def ancho(self):
        return self._ancho
        
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho if self._valid(ancho) else 0

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        self._alto = alto if self._valid(alto) else (0, print('Error el valor debe ser positivo'))[0]

    def __str__(self) -> str:
        return f'FiguraGeometrica [Ancho : {self.ancho}, Alto : {self.alto}]'
    
    def _valid(self, value):
        return value > 0

    @abstractmethod
    def calcular_area(self):
        pass