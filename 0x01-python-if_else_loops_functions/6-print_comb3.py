#!/usr/bin/python3
for num in range(9):
    for num2 in range(1, 10):
        if num == num2 or num > num2:
            continue
        elif num == 8 and num2 == 9:
            print("{}{}".format(num, num2))
        else:
            print("{}{}, ".format(num, num2), end="")
