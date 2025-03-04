Local ETL Pipeline – CSV to SQLite

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline built using Python. It extracts raw sales data from CSV files, applies transformations to clean and enrich the data, and loads the processed data into a SQLite database for storage and analysis.

Tech Stack
	•	Python 🐍
	•	pandas (data handling)
	•	sqlite3 (database loading)
	•	SQLite (lightweight local database)
	•	Git (version control)

 Project Structure:
 local-etl-pipeline/
├── data/
│   ├── raw/                # Raw CSV files
│   └── processed/          # Processed outputs (optional)
├── database/
│   └── sales.db            # SQLite database
├── etl/
│   ├── extract.py          # Extraction script
│   ├── transform.py        # Transformation script
│   └── load.py             # Loading script
├── notebooks/              # (Optional) Jupyter notebooks for EDA
├── run_pipeline.py         # Pipeline runner
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

