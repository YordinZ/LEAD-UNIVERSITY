class Reporte:
    def generar_datos(self):
        return "Datos del reporte"

    def guardar_archivo(self):
        print("Guardando reporte en archivo...")

    def enviar_correo(self):
        print("Enviando reporte por correo...")

# La clase Reporte está haciendo demasiadas cosas:
# genera datos
# guarda archivos
# envía correos
# Si cambia la forma de guardar archivos o de enviar correos, 
# habrá que modificar la misma clase.