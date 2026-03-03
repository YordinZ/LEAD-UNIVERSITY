#Clase documentada al estilo numpy
"""
Módulo de gestión de personas.

Contiene la clase Persona y funciones auxiliares
para crear y manipular objetos Persona dentro del sistema.
"""
class Persona:
    """
    Representa una persona con nombre y edad.

    Parameters
    ----------
    nombre : str
        Nombre de la persona.
    edad : int
        Edad de la persona.

    Attributes
    ----------
    _nombre : str
        Nombre almacenado de la persona.
    _edad : int
        Edad almacenada de la persona.
    """

    def __init__(self, nombre: str, edad: int):
        """
        Inicializa una nueva instancia de Persona.

        Parameters
        ----------
        nombre : str
            Nombre de la persona.
        edad : int
            Edad de la persona.
        """
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self) -> str:
        """
        Obtiene el nombre de la persona.

        Returns
        -------
        str
            Nombre actual de la persona.
        """
        return self._nombre

    @property
    def edad(self) -> int:
        """
        Obtiene la edad de la persona.

        Returns
        -------
        int
            Edad actual de la persona.
        """
        return self._edad

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        """
        Establece un nuevo nombre para la persona.

        Parameters
        ----------
        nuevo_nombre : str
            Nuevo nombre que se asignará a la persona.
        """
        self._nombre = nuevo_nombre

    @edad.setter
    def edad(self, nueva_edad: int) -> None:
        """
        Establece una nueva edad para la persona.

        Parameters
        ----------
        nueva_edad : int
            Nueva edad que se asignará a la persona.
        """
        self._edad = nueva_edad