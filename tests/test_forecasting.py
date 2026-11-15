from src.supplychainiq.forecasting import wape

def test_wape():
    assert wape([10, 20], [12, 18]) == 4 / 30
