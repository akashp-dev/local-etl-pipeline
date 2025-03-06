import pandas as pd
import logging

def transform_data(df):
    try:
        df = df.dropna()
        df['order_date'] = pd.to_datetime(df['order_date'])
        df['total_price'] = df['quantity'] * df['unit_price']
        
        # Data validation
        df = df[(df['quantity'] > 0) & (df['unit_price'] > 0)]
        
        logging.info(f"[TRANSFORM] Cleaned and validated {len(df)} records.")
        return df
    except Exception as e:
        logging.error(f"[TRANSFORM] Failed to transform data: {e}")
        return None
