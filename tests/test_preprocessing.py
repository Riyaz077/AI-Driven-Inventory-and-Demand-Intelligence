import pandas as pd,pytest
from src.supplychainiq.preprocessing import validate_demand
def test_negative_demand_rejected():
 with pytest.raises(ValueError): validate_demand(pd.DataFrame({"date":["2024-01-01"],"sku":["A"],"demand":[-1]}))
