#list
meat = ['Ham', 3.99, 50, "Sliced"]
#list
cheese = ["Chedder", 5.49, 100, "Sharp"]
#list
condiment = ['Mustard', 1.99, 75, "Spicy"]
#combined three list into one list 
deli_dept = [meat, cheese, condiment]
#printed initial list
print("Initial Deli List:", deli_dept)
# used if to see if ham was in meat list and value was 100 changed to 100
if 'Ham' in meat:
    meat[2] = 100
    #list
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
#append added seasonal_meat to deli_dept
deli_dept.append(seasonal_meat)
#removed condiment from deli_dept list
deli_dept.remove(condiment)
#sorted list alphabetically
deli_dept.sort()
#printed initial state of deli_dept with message
print("Updated Deli List:", deli_dept)