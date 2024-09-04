'''n = int(input("Enter you number: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print("")
'''


def print_square_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print("")

#Example Usage
a = int(input("Enter your number: "))
print_square_pattern(a)
