'''
n = int(input("Enter your Numbaer:"))
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for y in range(i):
        print("*", end=" ")
    for z in range(i+1):
        print("*", end= " ")
    print()
'''

def Hill_pattern(n):
    for a in range(n):
        for b in range(a,n):
            print(" ", end=" ")
        for c in range(a):
            print("*", end=" ")
        for d in range(a+1):
            print("*", end=" ")
        print()

a = int(input("Enter your number: "))
Hill_pattern(a)

