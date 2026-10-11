from bonjour import saluer


def test_saluer_ilia():
    assert saluer("ILIA") == "Bonjour ILIA !"


def test_saluer_vide():
    assert saluer("") == "Bonjour !"
