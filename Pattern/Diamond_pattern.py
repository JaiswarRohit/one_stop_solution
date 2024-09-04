'''
n = int(input("Enter your number: "))
for a in range(n):
    for b in range(a, n):
        print(" ", end=" ")
    for c in range(a):
        print("*", end=" ")
    for d in range(a+1):
        print("*", end=" ")
    print()
for a in range(n):
    for b in range(a+1):
        print(" ", end=" ")
    for c in range(a, n-1):
        print("*", end=" ")
    for d in range(a, n):
        print("*", end=" ")
    print()
'''
def Diamond_pattern(n):
    for a in range(n-1):
        for b in range(a, n):
            print(" ", end=" ")
        for c in range(a):
            print("*", end=" ")
        for d in range(a + 1):
            print("*", end=" ")
        print()
    for a in range(n):
        for b in range(a + 1):
            print(" ", end=" ")
        for c in range(a, n - 1):
            print("*", end=" ")
        for d in range(a, n):
            print("*", end=" ")
        print()

a = int(input("Enter your number: "))
Diamond_pattern(a)