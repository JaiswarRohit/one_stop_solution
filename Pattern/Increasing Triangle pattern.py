'''
n = int(input("Enter Your Number: "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print("")
'''

def increasing_triangle_pattern(n):
    for i in range(n): # Rows
        for j in range(i+1): #Columns
            print("*", end=" ")
        print("")
# Example Usage
a = int(input("Enter your number: "))
increasing_triangle_pattern(a)