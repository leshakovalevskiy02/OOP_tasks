# Задание 3
from functools import total_ordering

@total_ordering
class RomanNumeral:
    __roman_to_numbers = {"I": 1, "V": 5, "X": 10, "L": 50,
                       "C": 100, "D": 500, "M": 1000}
    __numbers_to_roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
                          40: "XL", 50: "L", 90: "XC", 100: "C",
                          400: "CD", 500: "D", 900: "CM", 1000: "M"}
    
    
    def __init__(self, number):
        """Принимает число в римской системе, например - I """
        self.number = number
        
    def __str__(self):
        return self.number
    
    def __int__(self):
        return self.__to_int(self.number)
    
    @classmethod
    def __to_int(cls, number):
        """Перевод числа из римской системы в целое число"""
        result = 0
        prev_dig = 0
        for char in number[::-1]:
            digit = cls.__roman_to_numbers[char]
            if prev_dig > digit:
                result -= digit
            else:
                result += digit
            prev_dig = digit
        return result
    
    @classmethod
    def __to_romanic(cls, number):
        """Перевод целого числа из целого числа в римскую систему"""
        result = ""
        for num in sorted(cls.__numbers_to_roman, reverse=True):
            if number >= num:
                coeff = number // num
                number %= num
                result += coeff * cls.__numbers_to_roman[num]
        return result
            
    def __eq__(self, other: "RomanNumeral"):
        if isinstance(other, RomanNumeral):
            return self.number == other.number
        return NotImplemented
    
    def __lt__(self, other: "RomanNumeral"):
        if isinstance(other, RomanNumeral):
            return int(self) < int(other)
        return NotImplemented
    
    def __add__(self, other: "RomanNumeral"):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.__to_romanic(int(self) + int(other)))
        return NotImplemented
    
    def __sub__(self, other: "RomanNumeral"):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.__to_romanic(int(self) - int(other)))
        return NotImplemented

# TEST_1:
a = RomanNumeral('X')
b = RomanNumeral('XII')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_2:
number = RomanNumeral('MXL') + RomanNumeral('MCDVIII') - RomanNumeral('I')

print(number)
print(int(number))

# TEST_3:
number = RomanNumeral('I') + RomanNumeral('II') + RomanNumeral('III') - RomanNumeral('V') 

print(number)
print(int(number))

# TEST_4:
roman = RomanNumeral('L')
print(roman.__eq__(1))
print(roman.__ne__(1.1))
print(roman.__gt__(range(5)))
print(roman.__lt__([1, 2, 3]))
print(roman.__ge__({4, 5, 6}))
print(roman.__le__({1: 'one'}))