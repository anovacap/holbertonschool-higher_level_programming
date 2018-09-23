#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is str:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                      'M': 1000, 'CM': 900, 'CD': 400,
                      'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
        tot = 0
        pr = 0
        minu = 0
        i = 1
        rln = len(roman_string)
        for rn in roman_string:
            if rln is 2 and i is rln:
                return roman_dict[rn] - pr
            tot += roman_dict[rn]
            if roman_dict[rn] > pr and i > 2:
                minu += (2 * pr)
            pr = roman_dict[rn]
            i += 1
        tot = tot - minu
        return tot
