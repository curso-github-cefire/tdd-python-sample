# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import numero_par

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_numero_par(self):
        assert es_par(4), "4 es par"
        assert es_par(0), "0 es par"
        assert es_par(-2), "-2, los negativos no son pares"
        assert not es_par(3), "3 no es par"
        assert not es_par(-1), "-1 no debería ser par"
