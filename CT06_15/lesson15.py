counter = 0
def increment_counter():
    global counter
    counter += 1
    print(f"Counter: {counter}")