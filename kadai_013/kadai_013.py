def cul_price(price,tax):
   total = price  + (price  * (tax/100))
   return total

print(cul_price(100,10))
    