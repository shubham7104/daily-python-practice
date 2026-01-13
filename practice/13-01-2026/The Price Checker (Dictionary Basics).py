def get_price(item_name):
    name = {
        "Roti" : 5,
        "Sabji" : "Free",
        "Rice" : 30,
        "Papad" : "once"
    }
    return name.get(item_name, "Item not found")
print(get_price("dal"))
