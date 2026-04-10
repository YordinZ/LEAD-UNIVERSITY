from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass
