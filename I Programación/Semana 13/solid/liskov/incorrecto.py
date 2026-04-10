class Ave:
    def volar(self):
        print("Estoy volando")


class Pinguino(Ave):
    def volar(self):
        raise Exception("Los pingüinos no vuelan")
    
# Pinguino hereda de Ave, pero no puede hacer algo que se espera de un ave en ese diseño: volar.
# Si en alguna parte del programa usamos un Pinguino como si fuera un Ave, el programa falla.