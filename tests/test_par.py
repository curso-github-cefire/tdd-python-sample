# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import esPar

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_esPar(self):
        assert esPar(8) == True
        assert esPar(1) == False
        assert esPar(5) == False
        assert esPar(2) == True
        assert esPar(3) == False
        assert esPar(2750) == True
        assert esPar(-54) == True
        assert esPar(22) == True
        assert esPar(888) == True
        assert esPar(1794830495907549234098546) == True
        