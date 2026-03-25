from abc import ABC, abstractmethod

class Figura(ABC):

    @abstractmethod
    def area(self):
        pass # el pass indica que se va a hacer una implementación a futuro