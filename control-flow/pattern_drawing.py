size = int(input("Enter the size of the pattern: "))

rows = size

while rows > 0:
    for i in range(size + 1):
        print("*", end="")
    print()
    rows -= 1