# #task (1)
# import time
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)

# #task (2)
# import time
# num = int(input("What is the seconds you want to countdown form? "))
# for i in range(num, 0 , -1):
#     print(i)
#     time.sleep(1)


# import random

# print(random.randint(1, 6 ))

# for i in range(1, 21):
#     print(0 , 9999)

# sols rng!!!
import random
import time

Worthless = 1
Trash = 2
Common = 4
Uncommon = 8
Rare = 16
Epic = 32
Unique = 64
Transcendent = 128
Legendary = 256
Mythic = 512
Exotic = 1024
 


Try = 0
while not Try == 1:
    num = 2
    print("Rolling...")
    Try = random.randint(1, num)
    if not Try == 1:
        print("You got Common!")
        time.sleep(1)
        print("Rolling...")
        time.sleep(1)
  
print("You got rare!")
    


