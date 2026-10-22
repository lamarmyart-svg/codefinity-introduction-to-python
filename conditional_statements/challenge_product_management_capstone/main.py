product_type = "perishable"
days_until_expiration = 5
stock_level = 60
if days_until_expiration <= 3 and stock_level > 50:
    print ("30% discount today")
elif  days_until_expiration <= 6 and stock_level >50:
    print ("20% discount today")
elif days_until_expiration > 6 and stock_level <= 50:
    print ("10% discount today")
else:
    print ("no discount available for non perishable items")
