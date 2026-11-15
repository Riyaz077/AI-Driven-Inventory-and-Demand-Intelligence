from .preprocessing import validate_demand
FEATURES=["lag_1","lag_7","lag_14","rolling_mean_7","rolling_std_7","day_of_week","month","promotion","sku_code"]
def build_features(df):
    x=validate_demand(df).sort_values(["sku","date"]).copy(); g=x.groupby("sku")["demand"]
    x["lag_1"]=g.shift(1); x["lag_7"]=g.shift(7); x["lag_14"]=g.shift(14)
    x["rolling_mean_7"]=g.transform(lambda s:s.shift(1).rolling(7,min_periods=3).mean())
    x["rolling_std_7"]=g.transform(lambda s:s.shift(1).rolling(7,min_periods=3).std())
    x["day_of_week"]=x.date.dt.dayofweek; x["month"]=x.date.dt.month
    if "promotion" not in x: x["promotion"]=0
    x["promotion"]=x["promotion"].fillna(0); x["sku_code"]=x.sku.astype("category").cat.codes
    return x.dropna(subset=FEATURES[:5]).reset_index(drop=True)
