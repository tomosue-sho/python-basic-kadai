def cul_price(price,tax):
    tax = price * 0.9
    tax2 = price - tax
    total = price + tax2
    return total

print(cul_price(100,"tax"))
    