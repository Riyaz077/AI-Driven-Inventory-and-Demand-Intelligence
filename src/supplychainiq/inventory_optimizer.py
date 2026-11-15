import math
def calculate_eoq(annual_demand,order_cost,annual_holding_cost_per_unit):
    if annual_demand<0 or order_cost<0 or annual_holding_cost_per_unit<=0: raise ValueError("Demand/order cost must be non-negative and holding cost positive.")
    return math.sqrt((2*annual_demand*order_cost)/annual_holding_cost_per_unit)
def calculate_safety_stock(daily_demand_std,lead_time_days,service_level_z=1.65):
    if min(daily_demand_std,lead_time_days,service_level_z)<0: raise ValueError("Inputs must be non-negative.")
    return service_level_z*daily_demand_std*math.sqrt(lead_time_days)
def calculate_reorder_point(avg_daily_demand,lead_time_days,safety_stock):
    if min(avg_daily_demand,lead_time_days,safety_stock)<0: raise ValueError("Inputs must be non-negative.")
    return avg_daily_demand*lead_time_days+safety_stock
def inventory_recommendation(*,avg_daily_demand,daily_demand_std,lead_time_days,current_stock,annual_demand,order_cost,annual_holding_cost_per_unit,service_level_z=1.65):
    ss=calculate_safety_stock(daily_demand_std,lead_time_days,service_level_z); rop=calculate_reorder_point(avg_daily_demand,lead_time_days,ss); eoq=calculate_eoq(annual_demand,order_cost,annual_holding_cost_per_unit)
    cover=current_stock/avg_daily_demand if avg_daily_demand>0 else None
    return {"eoq_units":round(eoq,2),"safety_stock_units":round(ss,2),"reorder_point_units":round(rop,2),"days_of_stock_cover":round(cover,2) if cover is not None else None,"inventory_status":"REORDER_REVIEW" if current_stock<=rop else "STOCK_ABOVE_REORDER_POINT"}
