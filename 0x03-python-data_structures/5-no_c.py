#!/usr/bin/python3
def no_c(my_string):
    c = "c"
    cap_c = "C"
    strlist = list(my_string)
    if c in strlist:
        poplist = strlist.index("c")
        del(strlist[poplist])
    if cap_c in strlist:
        poplist = strlist.index("C")
        del(strlist[poplist])
    newstr = "".join(strlist)
    return newstr
