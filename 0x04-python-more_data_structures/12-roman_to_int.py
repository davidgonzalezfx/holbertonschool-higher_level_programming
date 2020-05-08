#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or (type(roman_string) != str):
            return 0

    roman = 0
    nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    limit = len(roman_string)
    for ch in roman_string:
        for key, value in nums.items():
            if ch is key:
                if roman_string.index(ch) == limit - 1:
                    roman += value
                    break
                nxt = roman_string[roman_string.index(ch) + 1]
                if value >= nums.get(nxt):
                    roman += value
                else:
                    roman -= value
    return roman
