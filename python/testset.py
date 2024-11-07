basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
vegetables = {'potato', 'tomato', 'cucumber'}

print(basket)

print(basket | vegetables)
print(basket & vegetables)
print(basket - vegetables)


l1 = [1, 2, 3, 4, 5, [- 3, 4, 5], ['apple', 'banana', 'cherry']]
print(l1)

ls =  [1, 2, 3, 4, 5, [- 3, 4, 5], ['apple', 'banana', 'cherry']]
print(ls)

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

print(reverse("rohit"))