#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    tot = 0
    arg = sys.argv
    for i in range(len(arg) - 1):
        tot = tot + int(arg[i + 1])
    print(tot)
