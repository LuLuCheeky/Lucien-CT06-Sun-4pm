groceries = ["Apples", "Bread", "Carrots", "Dates", "Eggs", "Flour", "Grapes", "Herbs"]
groceries[7] = "Herbs"
groceries.append("Ice")
groceries.insert(1,"Bananas")
del(groceries[2])
print(groceries)
for grocery in groceries:
    print(grocery)
    if grocery == "Apples":
        print("I need 5 of these.")
    if grocery == "Carrots":
        print("I need 3 of these.")
    if grocery == "Grapes":
        print("Get the FarmFresh brand.")