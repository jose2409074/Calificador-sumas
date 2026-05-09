from src.logic import validar_operacion

def test_operacion_correcta():
    assert validar_operacion("24 + 30 = 54") == True

def test_operacion_incorrecta():
    assert validar_operacion("24 + 30 = 50") == False