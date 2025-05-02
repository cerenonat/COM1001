# 5.15 (Tuples Representing Invoices)
invoices = [
    ("001", "Hammer", 4, 9.99),
    ("002", "Nails", 100, 0.10),
    ("003", "Screwdriver", 2, 5.49),
    ("004", "Pliers", 1, 6.99)
]

for invoice in invoices:
    part_id, desc, qty, price = invoice
    total = qty * price
    print(f"ID: {part_id}, Item: {desc}, Qty: {qty}, Price: ${price:.2f}, Total: ${total:.2f}")
