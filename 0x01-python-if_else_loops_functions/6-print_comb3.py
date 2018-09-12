#!/usr/bin/python3
for num in range(10):
    for num2 in range(1, 10):
        if num == num2 or num > num2:
            continue
        print("{}{}, ".format(num, num2), end="")
        if num == 8 and num2 == 9:
            print("{}{}".format(num, num2))
