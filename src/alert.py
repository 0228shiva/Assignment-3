import logging

def get_low_stock_alerts(df):
    low_stock_items = df[df["ReorderQty"] > 0]
    logging.info(f"Found {len(low_stock_items)} low-stock items.")
    return low_stock_items
