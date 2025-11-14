SELECT 
    c.name AS customer,
    o.order_id,
    p.product_name,
    oi.quantity,
    pay.amount,
    pay.status
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN payments pay ON o.order_id = pay.order_id
LIMIT 50;
