'''
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0

Constraints:

0 <= n <= 5 * 106
Code By Saideep Shetty
'''

class Solution(object):
    def countPrimes(self, count):
        numbers = []
        for i in range(0, count+1):
            numbers.append(True)

        start = 2

        while start*start <= count:
            if numbers[start]:
                for i in range(start*2, count+1, start):
                    numbers[i] = False
            start += 1

        count_prime = 0

        for i in range(2, count):
            if numbers[i]:
                count_prime += 1

        return(count_prime)
