import math,pytest
from src.supplychainiq.inventory_optimizer import calculate_eoq,calculate_safety_stock,calculate_reorder_point,inventory_recommendation
def test_eoq(): assert calculate_eoq(1000,50,2)==pytest.approx(math.sqrt(50000))
def test_safety_stock(): assert calculate_safety_stock(4,9,2)==pytest.approx(24)
def test_rop(): assert calculate_reorder_point(10,5,20)==pytest.approx(70)
def test_invalid_holding_cost():
 with pytest.raises(ValueError): calculate_eoq(100,10,0)
def test_reorder_status():
 r=inventory_recommendation(avg_daily_demand=10,daily_demand_std=2,lead_time_days=5,current_stock=1,annual_demand=3650,order_cost=100,annual_holding_cost_per_unit=10)
 assert r["inventory_status"]=="REORDER_REVIEW"
