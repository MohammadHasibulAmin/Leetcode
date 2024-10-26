#https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
    
        def decimalToBinary(n):
            return "{0:b}".format(int(n))

        store = decimalToBinary(n)
        
        for i in store:
            if i == '1':
                count += 1

        return count