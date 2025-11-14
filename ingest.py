import pandas as pd
import sqlite3
import os

def ingest_into_sqlite():
    conn = sqlite3.connect("ecom.db")
    cur = conn.cursor()

    cur.executescript("""
    DROP TABLE IF EXISTS customers;
    DROP TABLE IF EXISTS products;
    DROP TABLE IF EXISTS orders;
    DROP TABLE IF EXISTS order_items;
    DROP TABLE IF EXISTS payments;

    CREATE TABLE customers(customer_id INTEGER, name TEXT, email TEXT);
    CREATE TABLE products(product_id INTEGER, product_name TEXT, price INTEGER);
    CREATE TABLE orders(order_id INTEGER, customer_id INTEGER, order_date TEXT);
    CREATE TABLE order_items(order_item_id INTEGER, order_id INTEGER, product_id INTEGER, quantity INTEGER);
    CREATE TABLE payments(payment_id INTEGER, order_id INTEGER, amount INTEGER, status TEXT);
    """)

    for table in ["customers","products","orders","order_items","payments"]:
        df = pd.read_csv(f"data/{table}.csv")
        df.to_sql(table, conn, if_exists="append", index=False)

    conn.commit()
    conn.close()
    print("Data ingested into sqlite database ecom.db")

if __name__ == "__main__":
    ingest_into_sqlite()
