product_type = "Dairy"
day_of_week = "wedensday"
if product_type == "Fruits" and day_of_week == "Monday":
    print ("10% discount on fruits today!")
elif product_type == "Vegetables" and  day_of_week == "Tuesday":
    print ("15% discount on Vegetables today!")
elif product_type == "other":
    print ("No discoount available")
else:
    print ("No special discounts today")