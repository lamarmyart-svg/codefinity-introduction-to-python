product_type = "Perishable"
days_until_expiration = 3
stock_level = 50

if product_type == "Perishable":
    # 30%: expires in 3 days or less AND stock > 50
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
    # 20%: expires in 4–6 days AND stock > 50
    elif 4 <= days_until_expiration <= 6 and stock_level > 50:
        print("20% discount applied")
    # 10%: stock <= 50 (or expires in 7+ days—but stock<=50 already covers this test)
    elif stock_level <= 50:
        print("10% discount applied")
else:
    print("No discount available for non-perishable items.")