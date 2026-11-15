def inventory_status(current_stock,reorder_point):
    if current_stock<0 or reorder_point<0: raise ValueError("Stock values must be non-negative.")
    return "REORDER_REVIEW" if current_stock<=reorder_point else "STOCK_ABOVE_REORDER_POINT"
