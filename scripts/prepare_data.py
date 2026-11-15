import argparse,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.supplychainiq.data_generator import generate_demand
p=argparse.ArgumentParser(); p.add_argument("--rows",type=int,default=12000); p.add_argument("--skus",type=int,default=12); p.add_argument("--output",default="data/sample/daily_demand.csv"); a=p.parse_args()
Path(a.output).parent.mkdir(parents=True,exist_ok=True); df=generate_demand(a.rows,a.skus); df.to_csv(a.output,index=False); print(f"Saved {len(df)} synthetic rows to {a.output}")
