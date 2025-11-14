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

<img width="547" height="191" alt="Screenshot 2025-11-14 152721" src="https://github.com/user-attachments/assets/1b672321-8800-47fb-88c8-7a546f1ed9be" />



python ingest.py

<img width="704" height="55" alt="Screenshot 2025-11-14 155918" src="https://github.com/user-attachments/assets/adc73dc8-52a5-481d-9859-0a3f5772e7be" />


query.sql

<img width="842" height="580" alt="Screenshot 2025-11-14 160207" src="https://github.com/user-attachments/assets/b0cd874e-dff2-4438-9610-8c68df332a65" />

running the command to see records
SELECT * FROM orders LIMIT 10;
<img width="819" height="440" alt="Screenshot 2025-11-14 160420" src="https://github.com/user-attachments/assets/a2e72ba1-bd36-49fb-9576-ed0dc0bad8b4" />





