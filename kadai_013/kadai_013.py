def cul_price(price,tax):
    tax = 0.1
    total = (price*tax) + price
    return total

print(cul_price(100,"tax"))
    