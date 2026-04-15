from main import gerar_tabuada

def test_tabuada_2():
    assert gerar_tabuada(2) == [2,4,6,8,10,12,14,16,18,20]

def test_tabuada_3():
    assert gerar_tabuada(3) == [3,6,9,12,15,18,21,24,27,30]
