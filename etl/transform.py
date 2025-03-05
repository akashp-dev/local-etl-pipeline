import pandas as pd

def transform_data(df):
    try:
        df = df.dropna()
        df['order_date'] = pd.to_datetime(df['order_date'])
        df['total_price'] = df['quantity'] * df['unit_price']
        print(f"[TRANSFORM] Cleaned and transformed {len(df)} rows.")
        return df
    except Exception as e:
        print(f"[ERROR] {e}")
        return None
