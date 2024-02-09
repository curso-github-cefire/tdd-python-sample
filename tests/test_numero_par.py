# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import numero_par

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para comprobar si un numero es par
    def test_numeropar(self):
        assert numero_par(4)
        assert numero_par(0) 
        assert numero_par(10) 
