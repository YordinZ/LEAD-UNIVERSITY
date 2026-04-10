class Configuracion:
    _instancia = None

# Patrón singleton
# Si no existe una instacia crea una nueva, si ya existe una instacia devuelve la existente
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.idioma = "es"
        return cls._instancia