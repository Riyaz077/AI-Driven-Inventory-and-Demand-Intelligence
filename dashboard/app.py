import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import streamlit as st, pandas as pd, plotly.express as px
from src.supplychainiq.inventory_optimizer import inventory_recommendation
st.set_page_config(page_title="SupplyChainIQ",page_icon="📦",layout="wide")
st.title("📦 SupplyChainIQ"); st.caption("Demand forecasting and inventory planning | Synthetic demonstration")
p=Path("data/sample/daily_demand.csv")
if not p.exists(): st.warning("Dataset missing. Run python scripts/prepare_data.py"); st.stop()
df=pd.read_csv(p,parse_dates=["date"]); sku=st.sidebar.selectbox("Select product",sorted(df.sku.unique())); product=df[df.sku==sku].sort_values("date")
a,b,c=st.columns(3); a.metric("Observed demand",f"{product.demand.sum():,} units"); b.metric("Average daily demand",f"{product.demand.mean():.1f}"); c.metric("Demand standard deviation",f"{product.demand.std():.1f}")
st.plotly_chart(px.line(product,x="date",y="demand",title=f"Daily demand — {sku}"),use_container_width=True)
st.subheader("Inventory planning calculator")
with st.form("inventory"):
 x,y,z=st.columns(3); avg=x.number_input("Average daily demand",min_value=0.0,value=float(product.demand.mean())); std=y.number_input("Daily demand standard deviation",min_value=0.0,value=float(product.demand.std())); lead=z.number_input("Lead time (days)",min_value=0,value=7); stock=x.number_input("Current stock",min_value=0.0,value=100.0); annual=y.number_input("Annual demand",min_value=0.0,value=float(product.demand.mean()*365)); order=z.number_input("Order cost",min_value=0.0,value=250.0); holding=x.number_input("Annual holding cost per unit",min_value=.01,value=35.0); service=y.number_input("Service-level z value",min_value=0.0,value=1.65); submitted=st.form_submit_button("Calculate recommendation")
if submitted:
 r=inventory_recommendation(avg_daily_demand=avg,daily_demand_std=std,lead_time_days=lead,current_stock=stock,annual_demand=annual,order_cost=order,annual_holding_cost_per_unit=holding,service_level_z=service); a,b,c=st.columns(3); a.metric("EOQ",f"{r['eoq_units']:.1f} units"); b.metric("Safety stock",f"{r['safety_stock_units']:.1f}"); c.metric("Reorder point",f"{r['reorder_point_units']:.1f}"); st.info(r["inventory_status"])
st.caption("Synthetic data and illustrative calculations. Validate assumptions before operational use.")
