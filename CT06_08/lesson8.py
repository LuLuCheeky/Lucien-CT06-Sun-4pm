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

Rare = 2

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
    


