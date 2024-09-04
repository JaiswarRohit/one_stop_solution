'''
n = int(input("Enter your Number: "))
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for z in range(i+1):
        print("*", end=" ")
    print()
'''

def right_trangle(n):
    for i in range(n):
        for j in range(i, n):
            print(" ", end =" ")
        for z in range(i+1):
            print("*", end=" ")
        print()

a = int(input("Enter your Enter: "))
right_trangle(a)