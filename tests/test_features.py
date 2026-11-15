import pandas as pd
from src.supplychainiq.feature_engineering import build_features
def test_lag_features_use_prior_values():
 df=pd.DataFrame([{"date":pd.Timestamp("2024-01-01")+pd.Timedelta(days=i),"sku":"A","demand":i+1,"promotion":0} for i in range(20)])
 out=build_features(df); row=out[out.date==pd.Timestamp("2024-01-15")].iloc[0]
 assert row.lag_1==14 and row.lag_7==8
