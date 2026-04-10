import json
import csv
import os

# Rutas base automáticas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

class FileConverter:
    """
    Singleton que convierte archivos JSON y CSV a diccionarios Python.

    Solo existe una instancia durante toda la ejecución del programa.
    Cualquier llamada a FileConverter() devuelve siempre la misma instancia.

    Ejemplo de uso:
        converter = FileConverter()
        data_json = converter.convertFromJson("datos.json")
        data_csv  = converter.convertFromCSV("datos.csv")
    """

    _instance = None

    def __new__(cls) -> 'FileConverter':
        if cls._instance is None:
            cls._instance = super(FileConverter, cls).__new__(cls)
        return cls._instance

    def convertFromJson(self, jsonFileStr: str) -> dict:
        """
        Lee un archivo JSON y lo convierte a un diccionario Python.
        Busca primero en DATA_DIR, luego en BASE_DIR, luego como ruta absoluta.
        """
        path = self._resolve_path(jsonFileStr)

        if not os.path.exists(path):
            raise FileNotFoundError(f"El archivo '{jsonFileStr}' no existe.")

        with open(path, encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError(f"El archivo JSON debe contener un objeto, pero se encontró: {type(data).__name__}")
        return data

    def convertFromCSV(self, csvFileStr: str) -> dict:
        """
        Lee un archivo CSV y retorna su contenido como diccionario Python.
        Busca primero en DATA_DIR, luego en BASE_DIR, luego como ruta absoluta.
        """
        path = self._resolve_path(csvFileStr)

        if not os.path.exists(path):
            raise FileNotFoundError(f"El archivo '{csvFileStr}' no existe.")

        result: dict = {}

        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                raise ValueError(f"El archivo CSV '{csvFileStr}' está vacío o no tiene encabezados.")

            primary_key = reader.fieldnames[0]

            for row in reader:
                clean_row = {
                    col.strip(): (val.strip() if val and val.strip() != "" else None)
                    for col, val in row.items()
                }
                key = clean_row[primary_key]
                result[key] = clean_row

        return result

    @staticmethod
    def _resolve_path(filename: str) -> str:
        """
        Resuelve la ruta del archivo en este orden:
          1. data/  (subcarpeta DATA_DIR)
          2. Junto al script (BASE_DIR)
          3. Como ruta absoluta o relativa al directorio de trabajo
        """
        # 1. Buscar en carpeta data/
        candidate = os.path.join(DATA_DIR, filename)
        if os.path.exists(candidate):
            return candidate

        # 2. Buscar junto al script
        candidate = os.path.join(BASE_DIR, filename)
        if os.path.exists(candidate):
            return candidate

        # 3. Ruta tal cual (absoluta o relativa al CWD)
        return filename

    @classmethod
    def reset(cls) -> None:
        cls._instance = None

    def __repr__(self) -> str:
        return f"<FileConverter Singleton id={id(self)}>"


# ======================================================================
# Programa de demostración
# ======================================================================

if __name__ == "__main__":
    import tempfile

    sample_json = {
        "empresa": "Acme Corp",
        "pais": "Costa Rica",
        "empleados": 150,
        "activo": True
    }

    sample_csv = (
        "id,nombre,departamento,salario\n"
        "E001,Ana Mora,Ingeniería,3500\n"
        "E002,Luis Pérez,Ventas,2800\n"
        "E003,María Solís,RRHH,\n"
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        json_path = os.path.join(tmpdir, "empresa.json")
        csv_path  = os.path.join(tmpdir, "empleados.csv")

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(sample_json, f)
        with open(csv_path, "w", encoding="utf-8") as f:
            f.write(sample_csv)

        print("=" * 55)
        print("  VERIFICACIÓN DEL PATRÓN SINGLETON")
        print("=" * 55)

        converter_a = FileConverter()
        converter_b = FileConverter()
        converter_c = FileConverter()

        print(f"  converter_a id: {id(converter_a)}")
        print(f"  converter_b id: {id(converter_b)}")
        print(f"  converter_c id: {id(converter_c)}")
        print(f"  ¿a is b?  →  {converter_a is converter_b}")
        print(f"  ¿b is c?  →  {converter_b is converter_c}")
        print(f"  Singleton garantizado: {converter_a is converter_b is converter_c}")

        print("\n" + "=" * 55)
        print("  convertFromJson()")
        print("=" * 55)

        json_data = converter_a.convertFromJson(json_path)
        print(f"  Tipo retornado : {type(json_data)}")
        print(f"  Contenido      : {json_data}")

        print("\n" + "=" * 55)
        print("  convertFromCSV()")
        print("=" * 55)

        csv_data = converter_a.convertFromCSV(csv_path)
        print(f"  Tipo retornado : {type(csv_data)}")
        print("  Contenido:")
        for key, value in csv_data.items():
            print(f"    {key!r:6} → {value}")

        print("\n" + "=" * 55)
        print("  MANEJO DE ERRORES")
        print("=" * 55)

        for ruta in ("inexistente.json", "inexistente.csv"):
            try:
                if ruta.endswith(".json"):
                    converter_a.convertFromJson(ruta)
                else:
                    converter_a.convertFromCSV(ruta)
            except FileNotFoundError as exc:
                print(f"  FileNotFoundError → {exc}")

    # ── Prueba con empresa.json ──────────────────────────────────────
    print("\n" + "=" * 55)
    print("  PRUEBA CON empresa.json")
    print("=" * 55)

    converter = FileConverter()
    data = converter.convertFromJson("empresa.json")
    print(f"  {data}")