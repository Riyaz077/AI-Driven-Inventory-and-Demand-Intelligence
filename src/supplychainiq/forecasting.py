from pathlib import Path
import json, joblib, numpy as np, pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error
from .feature_engineering import build_features,FEATURES
def wape(y_true,y_pred):
    denom=np.sum(np.abs(y_true)); return float(np.sum(np.abs(np.asarray(y_true)-np.asarray(y_pred)))/denom) if denom else 0.0
def train_and_evaluate(csv_path="data/sample/daily_demand.csv",model_path="models/random_forest.joblib",metrics_path="reports/evaluation/forecast_metrics.json",test_days=28):
    raw=pd.read_csv(csv_path,parse_dates=["date"]); feat=build_features(raw); end=feat.date.max(); cutoff=end-pd.Timedelta(days=test_days-1)
    train=feat[feat.date<cutoff]; test=feat[feat.date>=cutoff]
    if train.empty or test.empty: raise ValueError("Not enough data for requested chronological test window.")
    model=RandomForestRegressor(n_estimators=180,min_samples_leaf=2,random_state=42,n_jobs=-1); model.fit(train[FEATURES],train.demand)
    pred=np.maximum(0,model.predict(test[FEATURES])); naive=test.lag_7.to_numpy(); y=test.demand.to_numpy()
    metrics={"test_start":str(cutoff.date()),"test_end":str(end.date()),"rows_train":int(len(train)),"rows_test":int(len(test)),"random_forest":{"MAE":float(mean_absolute_error(y,pred)),"RMSE":float(np.sqrt(mean_squared_error(y,pred))),"WAPE":wape(y,pred)},"seasonal_naive_7d":{"MAE":float(mean_absolute_error(y,naive)),"RMSE":float(np.sqrt(mean_squared_error(y,naive))),"WAPE":wape(y,naive)}}
    Path(model_path).parent.mkdir(parents=True,exist_ok=True); Path(metrics_path).parent.mkdir(parents=True,exist_ok=True); joblib.dump({"model":model,"features":FEATURES},model_path); Path(metrics_path).write_text(json.dumps(metrics,indent=2),encoding="utf-8")
    return metrics
