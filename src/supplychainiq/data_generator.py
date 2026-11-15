import numpy as np
import pandas as pd

def generate_demand(rows=12000, n_skus=12, seed=42):
    rng=np.random.default_rng(seed)
    dates=pd.date_range("2023-01-01", periods=max(1, rows//n_skus), freq="D")
    records=[]; categories=["Grocery","Electronics","Home","Personal Care"]
    for i in range(n_skus):
        base=rng.uniform(8,45); trend=rng.uniform(-0.002,0.004); weekday=np.array([1.12,1.02,.98,1.0,1.08,1.22,1.18])
        for t,date in enumerate(dates):
            promo=int(rng.random()<.08); seasonal=1+.12*np.sin(2*np.pi*t/365.25)
            mean=max(.5,base*(1+trend*t)*weekday[date.dayofweek]*seasonal*(1.35 if promo else 1))
            records.append((date,f"SKU-{i+1:04d}",int(rng.poisson(mean)),round(float(rng.uniform(5,150)),2),promo,categories[i%4]))
    return pd.DataFrame(records,columns=["date","sku","demand","unit_price","promotion","category"]).sort_values(["sku","date"]).reset_index(drop=True)
