"""
models/videojuego.py
Clases de videojuegos con herencia, encapsulamiento, @property y polimorfismo.
"""


class VideoJuego:
    """Clase padre que representa un videojuego genérico."""

    def __init__(self, id, title, genre, price, esrb, consola, stock):
        self._id      = str(id)
        self._title   = str(title)
        self._genre   = str(genre)
        self._price   = float(price)
        self._esrb    = str(esrb).strip().upper()
        self._consola = str(consola).strip().lower()
        self._stock   = int(stock)

    # ── @property ──────────────────────────────

    @property
    def id(self) -> str:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, valor: str):
        if not valor.strip():
            raise ValueError("El título no puede estar vacío.")
        self._title = valor.strip()

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    def genre(self, valor: str):
        if not valor.strip():
            raise ValueError("El género no puede estar vacío.")
        self._genre = valor.strip()

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, valor: float):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._price = float(valor)

    @property
    def esrb(self) -> str:
        return self._esrb

    @esrb.setter
    def esrb(self, valor: str):
        VALIDOS = ['E', 'E10+', 'T', 'M', 'AO', 'RP']
        v = valor.strip().upper()
        if v not in VALIDOS:
            raise ValueError(f"ESRB inválido. Opciones: {VALIDOS}")
        self._esrb = v

    @property
    def consola(self) -> str:
        return self._consola

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = int(valor)

    # ── Polimorfismo (método sobreescrito en hijas) ──

    def descripcion_consola(self) -> str:
        """Retorna descripción de la plataforma. Sobreescrito en clases hijas."""
        return f"[Consola genérica] {self._title}"

    def plataforma_label(self) -> str:
        """Etiqueta de plataforma para mostrar en UI."""
        return self._consola.upper()

    # ── Serialización ──────────────────────────

    def to_dict(self) -> dict:
        return {
            "id":      self._id,
            "title":   self._title,
            "genre":   self._genre,
            "price":   self._price,
            "esrb":    self._esrb,
            "consola": self._consola,
            "stock":   self._stock,
        }

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"id={self._id!r}, title={self._title!r}, "
            f"price={self._price}, stock={self._stock})"
        )


# ══════════════════════════════════════════════
#  Clases hijas — Herencia + Polimorfismo
# ══════════════════════════════════════════════

class JuegoPS5(VideoJuego):
    """Videojuego para PlayStation 5."""

    def __init__(self, id, title, genre, price, esrb, stock):
        super().__init__(id, title, genre, price, esrb, 'ps5', stock)

    def descripcion_consola(self) -> str:
        return f"[PlayStation 5] {self._title}"

    def plataforma_label(self) -> str:
        return "PS5"


class JuegoXbox(VideoJuego):
    """Videojuego para Xbox."""

    def __init__(self, id, title, genre, price, esrb, stock):
        super().__init__(id, title, genre, price, esrb, 'xbox', stock)

    def descripcion_consola(self) -> str:
        return f"[Xbox Series X/S] {self._title}"

    def plataforma_label(self) -> str:
        return "Xbox"


class JuegoNintendo(VideoJuego):
    """Videojuego para Nintendo Switch."""

    def __init__(self, id, title, genre, price, esrb, stock):
        super().__init__(id, title, genre, price, esrb, 'switch', stock)

    def descripcion_consola(self) -> str:
        return f"[Nintendo Switch] {self._title}"

    def plataforma_label(self) -> str:
        return "Nintendo Switch"


# ══════════════════════════════════════════════
#  Factory — crea instancia correcta según consola
# ══════════════════════════════════════════════

def crear_juego(datos: dict) -> VideoJuego:
    """
    Recibe un dict normalizado y retorna la instancia
    de la clase hija correspondiente (polimorfismo en acción).
    """
    consola = str(datos.get('consola', '')).strip().lower()
    args = (
        datos['id'],
        datos['title'],
        datos['genre'],
        datos['price'],
        datos['esrb'],
        datos['stock'],
    )
    if consola == 'ps5':
        return JuegoPS5(*args)
    elif consola == 'xbox':
        return JuegoXbox(*args)
    elif consola == 'switch':
        return JuegoNintendo(*args)
    else:
        return VideoJuego(
            datos['id'], datos['title'], datos['genre'],
            datos['price'], datos['esrb'], consola, datos['stock']
        )
