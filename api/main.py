from fastapi import FastAPI
from pydantic import BaseModel,Field
from src.supplychainiq.recommendations import recommend_for_product
app=FastAPI(title="SupplyChainIQ API",version="0.1.0",description="Inventory planning calculator demonstration.")
class Request(BaseModel):
 sku:str
 avg_daily_demand:float=Field(ge=0)
 daily_demand_std:float=Field(ge=0)
 lead_time_days:float=Field(ge=0)
 current_stock:float=Field(ge=0)
 annual_demand:float=Field(ge=0)
 order_cost:float=Field(ge=0)
 annual_holding_cost_per_unit:float=Field(gt=0)
 service_level_z:float=Field(default=1.65,ge=0)
@app.get("/health")
def health(): return {"status":"ok","mode":"synthetic_demo"}
@app.post("/recommendation")
def recommendation(payload:Request): return {"sku":payload.sku,**recommend_for_product(payload)}
