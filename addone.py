def addone(x):
    return int(x) + 1

def add(x,y): 
    return int(x) + int(y)

if __name__ == "__main__":
    val = input("enter a number:")
    print(f'{val} + 1 = {addone(val)}')