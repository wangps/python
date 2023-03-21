def addone(x):
    return int(x) + 1

if __name__ == "__main__":
    val = input("enter a number:")
    print(f'{val} + 1 = {addone(val)}')