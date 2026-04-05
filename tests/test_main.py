from src.main import tambah

def test_tambah():
    assert tambah(10, 5) == 15
    assert tambah(-1, 1) == 0