'''
n = int(input("Enter your number: "))
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(i+1, n+1):
        print("*", end=" ")
    print()
'''

def rigth_sided_Trigle(n):
    for i in range(n):
        for j in range(i):
            print(" ", end= " ")
        for z in range(i, n):
            print("*", end=" ")
        print()

a = int(input("Enter your number: "))
rigth_sided_Trigle(a)
