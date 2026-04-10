import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba
        self.calc = Calculadora()

    # -------- SUMAR --------
    def test_sumar_numeros_positivos(self):
        self.assertEqual(self.calc.sumar(2, 3), 5)

    def test_sumar_con_cero(self):
        self.assertEqual(self.calc.sumar(5, 0), 5)

    def test_sumar_negativos(self):
        self.assertEqual(self.calc.sumar(-2, -3), -5)

    # -------- RESTAR --------
    def test_restar_numeros(self):
        self.assertEqual(self.calc.restar(10, 4), 6)

    def test_restar_resultado_negativo(self):
        self.assertEqual(self.calc.restar(3, 5), -2)

    # -------- MULTIPLICAR --------
    def test_multiplicar_numeros(self):
        self.assertEqual(self.calc.multiplicar(4, 3), 12)

    def test_multiplicar_por_cero(self):
        self.assertEqual(self.calc.multiplicar(5, 0), 0)

    # -------- DIVIDIR --------
    def test_dividir_numeros(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_dividir_resultado_decimal(self):
        self.assertEqual(self.calc.dividir(7, 2), 3.5)

    def test_dividir_entre_cero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)


if __name__ == "__main__":
    unittest.main()