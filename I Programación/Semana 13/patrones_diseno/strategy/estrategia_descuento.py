from abc import ABC, abstractmethod

# Estrategia abstracta
class EstrategiaDescuento(ABC):
    @abstractmethod
    def aplicar_descuento(self, total):
        pass