groceries = ["Apples", "Bread", "Carrots", "Dates", "Eggs", "Flour", "Grapes", "Herbs"]
groceries[7] = "Herbs"
groceries.append("Ice")
groceries.insert(1,"Bananas")
del(groceries[2])

# Task 2: List of groceries (part 2)
# 1. Use a 'for' loop and print out all the groceries on your list
# 2. If grocery == "Apples", print "<grocery name>: I need 5 of these"
# 3. If grocery == "Carrots", print "<grocery name>: I need 3 of
#    these"
# 4. If name == "Grapes", print "<grocery name>: Get the FarmFresh
#    brand"
for grocery in groceries:
    print(grocery)
    if grocery == "Apples":
        print("I need 5 of these.")
    elif grocery == "Carrots":
        print("I need 3 of these.")
    elif grocery == "Grapes":
        print("Get the FarmFresh brand.")