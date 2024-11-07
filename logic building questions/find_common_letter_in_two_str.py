def common_letter():
    str1 = input("Enter your str1: ")
    str2 = input("Enter your str2: ")

    s1 = set(str1)
    s2 = set(str2)
    list = s1 & s2
    print(list)


common_letter()