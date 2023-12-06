#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_nums = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
                  'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
                  'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    result = 0
    if isinstance(roman_string, str) and roman_string:
        r = roman_string
        lgz = len(r)
        flag = 0
        for i in range(lgz):
            if flag == 1:
                flag = 0
                continue
            if r[i] == "I":
                if (i < lgz - 1) and r[i + 1] in "VX":
                    result += roman_nums[r[i] + r[i + 1]]
                    flag = 1
                else:
                    result += roman_nums[r[i]]
            elif r[i] == "X":
                if (i < lgz - 1) and r[i + 1] in "LC":
                    result += roman_nums[r[i] + r[i + 1]]
                    flag = 1
                else:
                    result += roman_nums[r[i]]
            elif r[i] == "C":
                if (i < lgz - 1) and r[i + 1] in "DM":
                    result += roman_nums[r[i] + r[i + 1]]
                    flag = 1
                else:
                    result += roman_nums[r[i]]
            else:
                result += roman_nums[r[i]]
    return (result)
