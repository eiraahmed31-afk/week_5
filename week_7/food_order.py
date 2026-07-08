def calculate_total(price, quantity):
    if price < 0:
        raise ValueError("invalid price")
    if quantity < 0:
        raise ValueError("invalid quantity")

    return price * quantity