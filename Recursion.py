
global steps=0

def walk():
    steps=steps+1
    if steps==100:
        return
    print("r")
    walk()

walk()
