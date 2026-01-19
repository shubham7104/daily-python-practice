def calculate_total(cart):
    total = 0
    for item in cart:
        total += item.get("price")

    return total
cart = [
    {"item": "Laptop", "price": 1000},
    {"item": "Mouse", "price": 20},
    {"item": "Keyboard", "price": 50}
]

'''TEST
print(calculate_total(cart)) 
'''
