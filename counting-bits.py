
"""Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 """

import math

def convertToBinary(num):
    bin = []
    while num!=0:
        if num == 1:
            bin.append(1)
            break
        elif num % 2 == 1:
            bin.append(1)
        else:
            bin.append(0)
        num = math.floor(num / 2)
    return bin[::-1] 

def countingBits(n):
    sumOfBits = [0]
    for i in range(1, n+1):
        print(i)
        bit = convertToBinary(i)
        sum = 0
        for j in bit:
            if j == 1:
                sum += 1
        sumOfBits.append(sum)
    print(sumOfBits)
    
countingBits(5)
