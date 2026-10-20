# initial conditions
totalCost = 150
#applying discounts based on purchase amount
if totalCost >= 200:
    print ("20% discount")
elif totalCost >= 100:
    print ("10% discount applied")
else:
    print ("no discount for purchases under $100")