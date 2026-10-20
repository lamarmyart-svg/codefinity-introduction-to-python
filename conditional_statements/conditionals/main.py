# initial conditions
product = 'Non-Perishable'
stock = 70
daysdelivered = 3
# Determine the handling of products based on type and condition
if product == "Perishable":
    if daysdelivered >= 4:
        print ("Not fresh - initiate discount")
    else:
        print ("product is fresh")
elif product == "Non - Periishable":
    if stock > 100:
        print ("Consider discount")
    else:
        Print ("No discount needed")