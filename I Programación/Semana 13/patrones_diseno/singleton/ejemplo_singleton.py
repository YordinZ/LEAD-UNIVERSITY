from configuracion import Configuracion

# Uso
config1 = Configuracion()
config2 = Configuracion()

config1.idioma = "en"

print(config1.idioma)
print(config2.idioma)
print(config1 is config2) # A pesar de llamar al constructor 2 veces, ambas variables apuntan al mismo objeto