thing = input("What is the item you are buying? ")
px = int(input("How much is the " + thing + "? "))
if px <= 5:
    print("Sure buy it why not???????????? ITS SO CHEAPPPP")
elif px <= 50:
    print("Are you really sure you want the" , thing + ".")
elif px <= 500:
    print("Where are you even getting the money from?? Your slary is only 125 or something a year!")
elif px > 501:
    print("Don't buy it unless you have money from the shark loaners! (Why do you even loan money from the sharks in the first place you cooked lol.)")