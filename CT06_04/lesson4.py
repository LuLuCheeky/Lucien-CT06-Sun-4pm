# Red = 1
# blue = 2
# green = 3
# Name = input("What is your name? ")
# NumRed = int(input("How many red plates? "))
# NumBlue = int(input("How many red plates? "))
# NumGreen = int(input("How many red plates? "))
# total = (Red * NumRed) + (blue * NumBlue) + (green * NumGreen)
# print(Name + ", you owe us $" + str(total))


def crash():
        '''\
        crash the Python interpreter...
        '''
        i = ctypes.c_char('a')
        j = ctypes.pointer(i)
        c = 0
        while True:
                j[c] = 'a'
                c += 1
        j