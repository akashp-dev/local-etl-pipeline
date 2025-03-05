import pandas as pd

def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"[EXTRACT] Extracted {len(df)} rows from {file_path}")
        return df
    except Exception as e:
        print(f"[ERROR] {e}")
        return None
