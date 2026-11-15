import pandas as pd
REQUIRED={"date","sku","demand"}
def validate_demand(df):
    missing=REQUIRED-set(df.columns)
    if missing: raise ValueError(f"Missing required columns: {sorted(missing)}")
    out=df.copy(); out["date"]=pd.to_datetime(out["date"],errors="coerce"); out["demand"]=pd.to_numeric(out["demand"],errors="coerce")
    out=out.dropna(subset=["date","sku","demand"])
    if (out.demand<0).any(): raise ValueError("Demand cannot be negative.")
    if out.duplicated(["date","sku"]).any(): raise ValueError("Duplicate date/SKU observations found.")
    return out.sort_values(["sku","date"]).reset_index(drop=True)
