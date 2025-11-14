# E-Commerce Data Processing Project

This project is a small end-to-end workflow where I generate synthetic e-commerce data, load it into an SQLite database, and run a SQL JOIN query to combine information from multiple tables.  
The goal was to complete the entire workflow inside **Cursor IDE**, document the steps, and push everything to GitHub.

---

## ⭐ What this project contains

- data_gen.py — creates 5 synthetic CSV files (customers, products, orders, order_items, payments)
- ingest.py — loads all CSVs into an SQLite database called `ecom.db`
- query.sql — a join query that pulls combined e-commerce data
- data folder — holds all generated CSV files
- ecom.db — database created after running ingestion
- README.md — explanation of work and instructions
- screenshots  — proof of running everything in Cursor

---

## ⭐ How to run the project (Step-by-Step)

### 1. Generate synthetic data
Run this in the terminal:

```bash
python data_gen.py
This will create the following CSVs inside the data/ folder:

customers.csv

products.csv

orders.csv

order_items.csv

payments.csv

<img width="1484" height="914" alt="image" src="https://github.com/user-attachments/assets/ddf02690-7c53-4747-800e-e28970685d06" />

python ingest.py

<img width="704" height="55" alt="image" src="https://github.com/user-attachments/assets/2f01a303-628f-46b5-8590-e1a646c571e9" />

query.sql

<img width="842" height="580" alt="image" src="https://github.com/user-attachments/assets/85c4a598-4c5e-436a-805f-5964eff5a80d" />

running the command to see records
SELECT * FROM orders LIMIT 10;
<img width="819" height="440" alt="image" src="https://github.com/user-attachments/assets/265a82b8-96ec-4266-84b9-43d8c32f144d" />



