'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 '''

 class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        output = [[1]]
        for i in range(1, numRows):
            temp = list(output[-1])
            temp.insert(0, '0')
            temp.append('0')
            op = []
            for j in range(len(temp)-1):
                num = int(temp[j]) + int(temp[j+1])
                op.append(num)
            output.append(op)
        return output