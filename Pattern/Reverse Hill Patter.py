'''
n = int(input("Enter your name: "))
for a in range(n):
    for b in range(a):
        print(" ", end=" ")
    for c in range(a, n):
        print("*", end=" ")
    for d in range(a+1, n):
        print("*", end=" ")
    print()
'''
def reverse_hill_patter(n):
    for a in range(n):
        for b in range(a):
            print(" ", end=" ")
        for c in range(a, n):
            print("*", end=" ")
        for d in range(a+1, n):
            print("*", end = " ")
        print()

i = int(input("Enter your number: "))
reverse_hill_patter(i)

