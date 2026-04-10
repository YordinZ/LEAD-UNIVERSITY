class Reporte:
    def generar_datos(self):
        return "Datos del reporte"


class GuardadorReporte:
    def guardar_archivo(self, contenido):
        print(f"Guardando en archivo: {contenido}")


class EnviadorCorreo:
    def enviar(self, contenido):
        print(f"Enviando por correo: {contenido}")


# Cada clase tiene una tarea clara:
# - Reporte genera información
# - GuardadorReporte guarda información
# - EnviadorCorreo envía información

reporte = Reporte()
datos = reporte.generar_datos()

guardador = GuardadorReporte()
guardador.guardar_archivo(datos)

correo = EnviadorCorreo()
correo.enviar(datos)