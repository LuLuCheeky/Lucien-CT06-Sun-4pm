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

Raritys = [
    "Worthless",
    "Trash",
    "Common",
    "Uncommon",
    "Rare",
    "Epic",
    "Unique",
    "Gemstone",
    "Transcendent",
    "Legendary",
    "Mythical",
    "Exotic", 
    "Divine",
    "Heavenly"
    "Arcane"
]

RarityChance = [
    2,
    4,
    8,
    16,
    32,
    64,
    128,
    256,
    512,
    1024,
    2048,
    4096,
    8192,
    16384
]

num = 2
Rarity = 2
Try = 0
RarityLoop = 2
while not Try == 1:
    while not Rarity == num:
        RarityLoop = RarityLoop + RarityLoop

    print("Rolling...")
    Try = random.randint(1, num)
    if not Try == 1:
        print("You got" ,)
        time.sleep(1)
    num = num + num
    Check = 2

    


