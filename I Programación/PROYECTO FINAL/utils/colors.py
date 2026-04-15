"""
utils/colors.py
Constantes ANSI y helpers de color/formato para la terminal.
"""
import re

# ── Códigos ANSI ──────────────────────────────
RESET    = '\033[0m'
NEGRITA  = '\033[1m'
DIM      = '\033[2m'

VERDE    = '\033[92m'
AMARILLO = '\033[93m'
ROJO     = '\033[91m'
CYAN     = '\033[96m'
MAGENTA  = '\033[95m'
AZUL     = '\033[94m'
GRIS     = '\033[90m'
BLANCO   = '\033[97m'

# ── Helpers de mensaje ────────────────────────
def ok(msg: str)       -> str: return f"{VERDE}{NEGRITA}✅ {msg}{RESET}"
def err(msg: str)      -> str: return f"{ROJO}{NEGRITA}❌ {msg}{RESET}"
def warn(msg: str)     -> str: return f"{AMARILLO}⚠️  {msg}{RESET}"
def info(msg: str)     -> str: return f"{AZUL}ℹ️  {msg}{RESET}"
def titulo(msg: str)   -> str: return f"{CYAN}{NEGRITA}{msg}{RESET}"
def dim(msg: str)      -> str: return f"{GRIS}{msg}{RESET}"
def precio(v: float)   -> str: return f"{AMARILLO}${v:.2f}{RESET}"
def resaltar(msg: str) -> str: return f"{MAGENTA}{NEGRITA}{msg}{RESET}"

def linea(char: str = '─', ancho: int = 60, color: str = GRIS) -> str:
    return f"{color}{char * ancho}{RESET}"

# ── Helpers ANSI-aware ────────────────────────
def len_visible(s: str) -> int:
    """Longitud real ignorando códigos de escape ANSI."""
    return len(re.sub(r'\033\[[0-9;]*m', '', s))

def pad(s: str, ancho: int, alinear: str = 'izq') -> str:
    """Rellena con espacios considerando solo caracteres visibles."""
    espacios = max(0, ancho - len_visible(s))
    return (' ' * espacios + s) if alinear == 'der' else (s + ' ' * espacios)

# ── Color por tipo ────────────────────────────
def color_esrb(esrb: str) -> str:
    mapa = {
        'E':    f"{VERDE}{NEGRITA}E{RESET}",
        'E10+': f"{VERDE}E10+{RESET}",
        'T':    f"{AMARILLO}{NEGRITA}T{RESET}",
        'M':    f"{ROJO}{NEGRITA}M{RESET}",
        'AO':   f"{MAGENTA}{NEGRITA}AO{RESET}",
        'RP':   f"{GRIS}RP{RESET}",
    }
    return mapa.get(esrb.strip().upper(), f"{GRIS}{esrb}{RESET}")

def color_stock(stock: int) -> str:
    if stock == 0:
        return f"{ROJO}{NEGRITA}{stock}{RESET}"
    elif stock <= 3:
        return f"{AMARILLO}{stock}{RESET}"
    return f"{VERDE}{stock}{RESET}"

def color_consola(consola: str) -> str:
    mapa = {
        'ps5':    f"{AZUL}{NEGRITA}PS5{RESET}",
        'xbox':   f"{VERDE}{NEGRITA}Xbox{RESET}",
        'switch': f"{ROJO}{NEGRITA}Nintendo{RESET}",
    }
    return mapa.get(consola.strip().lower(), consola)
