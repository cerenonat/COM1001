# 8.1 (Check Protection)

amount = input("Enter the check amount: ")

try:
    amount_float = float(amount)
    protected = f"{amount_float:*>10.2f}"
    print("Check-protected amount:", protected)
except ValueError:
    print("Invalid amount. Please enter a number.")
