# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import factorial

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_factorial(self):
        assert factorial(8) == 40320
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(0) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(10) == 3628800
        

    def test_lanza_except(self):

        with pytest.raises(ValueError) as exception_info:
            factorial(-1)
        assert str(exception_info.value) == 'El parámetro debe ser mayor o igual que 0'  

        with pytest.raises(ValueError) as exception_info:
            factorial(-2)
        assert str(exception_info.value) == 'El parámetro debe ser mayor o igual que 0'        


       
        