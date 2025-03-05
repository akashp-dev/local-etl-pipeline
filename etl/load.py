import sqlite3

def load_data(df, db_file, table_name):
    try:
        conn = sqlite3.connect(db_file)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        print(f"[LOAD] Loaded data into '{table_name}' table.")
    except Exception as e:
        print(f"[ERROR] {e}")
