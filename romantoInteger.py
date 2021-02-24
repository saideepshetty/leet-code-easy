'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
Code By Saideep Shetty
'''
class Solution:
    def romanToInt(self, s):
        numberslist = list(s)
        listlen = len(numberslist)
        list2 =[]
        for i in numberslist:
            if i == 'I':
                 list2.append(int('1'))
            elif i == 'V':
                list2.append(int('5'))
            elif i == 'X':
                list2.append(int('10'))
            elif i == 'L':
                list2.append(int('50'))
            elif i == 'C':
                list2.append(int('100'))
            elif i == 'D':
                list2.append(int('500'))
            elif i == 'M':
                list2.append(int('1000'))
            else:
                continue
        sum = 0
        for i in range(len(list2)):
            if i == 0:
                sum = sum + list2[i]
            else:
                if list2[i-1] == 1 and list2[i] == 5 or list2[i-1] == 1 and list2[i] == 10:
                    sum = sum + list2[i] - list2[i-1] - list2[i-1]
                elif list2[i-1] == 10 and list2[i] == 50 or list2[i-1] == 10 and list2[i] == 100:
                    sum = sum + list2[i] - list2[i-1] - list2[i-1]
                elif list2[i-1] == 100 and list2[i] == 500 or list2[i-1] == 100 and list2[i] == 1000:
                    sum = sum + list2[i] - list2[i-1] - list2[i-1]
                else:
                    sum = sum + list2[i]
        return sum
