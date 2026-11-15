import pandas as pd
from .preprocessing import validate_demand
def load_demand(path): return validate_demand(pd.read_csv(path,parse_dates=["date"]))
