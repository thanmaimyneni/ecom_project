import pandas as pd
import numpy as np
import os

def generate_data():
    os.makedirs("data", exist_ok=True)

    customers = pd.DataFrame({
        "customer_id": range(1, 51),
        "name": [f"Customer_{i}" for i in range(1, 51)],
        "email": [f"user{i}@mail.com" for i in range(1,51)]
    })

    products = pd.DataFrame({
        "product_id": range(1, 21),
        "product_name": [f"Product_{i}" for i in range(1,21)],
        "price": np.random.randint(100, 2000, 20)
    })

    orders = pd.DataFrame({
        "order_id": range(1, 101),
        "customer_id": np.random.randint(1, 51, 100),
        "order_date": pd.date_range("2024-01-01", periods=100).astype(str)
    })

    order_items = pd.DataFrame({
        "order_item_id": range(1, 201),
        "order_id": np.random.randint(1, 101, 200),
        "product_id": np.random.randint(1, 21, 200),
        "quantity": np.random.randint(1, 5, 200)
    })

    payments = pd.DataFrame({
        "payment_id": range(1, 101),
        "order_id": range(1, 101),
        "amount": np.random.randint(100, 3000, 100),
        "status": np.random.choice(["SUCCESS", "FAILED"], 100)
    })

    customers.to_csv("data/customers.csv", index=False)
    products.to_csv("data/products.csv", index=False)
    orders.to_csv("data/orders.csv", index=False)
    order_items.to_csv("data/order_items.csv", index=False)
    payments.to_csv("data/payments.csv", index=False)
    print("Synthetic ecommerce data generated.")

if __name__ == "__main__":
    generate_data()
