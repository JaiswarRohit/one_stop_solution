'''
n = int(input("Enter your number:"))
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    print("")
'''

def Decreasing_triangle_pattern(n):
    for i in range(n):
        for j in range(i, n):
            print("*", end=" ")
        print("")

# Example Usage
a = int(input("Enter your number: "))
Decreasing_triangle_pattern(a)