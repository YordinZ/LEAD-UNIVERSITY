import unittest
from libreria import LibreriaDeMangas


class TestLibreriaDeMangas(unittest.TestCase):

    def setUp(self):
        self.libreria = LibreriaDeMangas()

    # -----------------------------
    # Pruebas de __init__
    # -----------------------------
    def test_inicia_con_mangas_por_defecto(self):
        mangas = self.libreria.obtener_todos_los_mangas()

        self.assertIn("Naruto", mangas)
        self.assertIn("One Piece", mangas)
        self.assertIn("Attack on Titan", mangas)
        self.assertIn("Demon Slayer", mangas)

        self.assertEqual(mangas["Naruto"], 3)
        self.assertEqual(mangas["One Piece"], 5)
        self.assertEqual(mangas["Attack on Titan"], 2)
        self.assertEqual(mangas["Demon Slayer"], 4)

    # -----------------------------
    # Pruebas de agregar_manga
    # -----------------------------
    def test_agregar_manga_nuevo(self):
        self.libreria.agregar_manga("Bleach")
        self.assertTrue(self.libreria.existe_manga("Bleach"))
        self.assertEqual(self.libreria.obtener_cantidad("Bleach"), 1)

    def test_agregar_manga_repetido_incrementa_contador(self):
        cantidad_inicial = self.libreria.obtener_cantidad("Naruto")
        self.libreria.agregar_manga("Naruto")
        self.assertEqual(self.libreria.obtener_cantidad("Naruto"), cantidad_inicial + 1)

    def test_agregar_manga_con_nombre_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            self.libreria.agregar_manga("")

    def test_agregar_manga_con_espacios_lanza_error(self):
        with self.assertRaises(ValueError):
            self.libreria.agregar_manga("   ")

    # -----------------------------
    # Pruebas de obtener_cantidad
    # -----------------------------
    def test_obtener_cantidad_de_manga_existente(self):
        self.assertEqual(self.libreria.obtener_cantidad("One Piece"), 5)

    def test_obtener_cantidad_de_manga_inexistente(self):
        self.assertEqual(self.libreria.obtener_cantidad("Dragon Ball"), 0)

    def test_obtener_cantidad_con_nombre_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            self.libreria.obtener_cantidad("")

    # -----------------------------
    # Pruebas de existe_manga
    # -----------------------------
    def test_existe_manga_devuelve_true_si_existe(self):
        self.assertTrue(self.libreria.existe_manga("Naruto"))

    def test_existe_manga_devuelve_false_si_no_existe(self):
        self.assertFalse(self.libreria.existe_manga("Death Note"))

    def test_existe_manga_con_nombre_invalido_lanza_error(self):
        with self.assertRaises(ValueError):
            self.libreria.existe_manga("   ")

    # -----------------------------
    # Pruebas de eliminar_manga
    # -----------------------------
    def test_eliminar_manga_reduce_cantidad_si_hay_mas_de_uno(self):
        cantidad_inicial = self.libreria.obtener_cantidad("Demon Slayer")
        self.libreria.eliminar_manga("Demon Slayer")
        self.assertEqual(self.libreria.obtener_cantidad("Demon Slayer"), cantidad_inicial - 1)

    def test_eliminar_manga_lo_borra_si_solo_hay_uno(self):
        self.libreria.agregar_manga("Bleach")
        self.assertEqual(self.libreria.obtener_cantidad("Bleach"), 1)

        self.libreria.eliminar_manga("Bleach")
        self.assertFalse(self.libreria.existe_manga("Bleach"))
        self.assertEqual(self.libreria.obtener_cantidad("Bleach"), 0)

    def test_eliminar_manga_inexistente_lanza_error(self):
        with self.assertRaises(ValueError):
            self.libreria.eliminar_manga("Slam Dunk")

    def test_eliminar_manga_con_nombre_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            self.libreria.eliminar_manga("")

    # -----------------------------
    # Pruebas de obtener_todos_los_mangas
    # -----------------------------
    def test_obtener_todos_los_mangas_devuelve_diccionario(self):
        mangas = self.libreria.obtener_todos_los_mangas()
        self.assertIsInstance(mangas, dict)

    def test_obtener_todos_los_mangas_devuelve_copia(self):
        mangas = self.libreria.obtener_todos_los_mangas()
        mangas["Naruto"] = 100

        # Verifica que no se modificó el original
        self.assertEqual(self.libreria.obtener_cantidad("Naruto"), 3)


if __name__ == "__main__":
    unittest.main()