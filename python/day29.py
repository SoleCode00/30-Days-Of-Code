# Task
'''
Given set S={1, 2, 3,..., N}. Find two integers, A and B (where A < B), from set S such that the value of A&B is the maximum possible and also less than a given integer, K. In this case, & represents the bitwise AND operator.

Function Description
Complete the bitwiseAnd function in the editor below.

bitwiseAnd has the following paramter(s):
- int N: the maximum integer to consider
- int K: the limit of the result, inclusive
'''

# Sample Input
'''
The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines defines a test case as 2 space-separated integers, N and K, respectively.

STDIN   Function
-----   --------
3       T = 3
5 2     N = 5, K = 2
8 5     N = 8, K = 5
2 2     N = 8, K = 5
'''

# Sample Output
'''
1
4
0
'''

# Explanation
'''
N=5, K=2 S={1,2,3,4,5}

All possible values of A and B are:
1.  A = 1,   B = 2;   A & B = 0
2.  A = 1,   B = 3;   A & B = 1
3.  A = 1,   B = 4;   A & B = 0
4.  A = 1,   B = 5;   A & B = 1
5.  A = 2,   B = 3;   A & B = 2
6.  A = 2,   B = 4;   A & B = 0
7.  A = 2,   B = 5;   A & B = 0
8.  A = 3,   B = 4;   A & B = 0
9.  A = 3,   B = 5;   A & B = 1
10. A = 4,   B = 5;   A & B = 4
'''

# Code

#!/bin/python3
import math
import os
import random
import re
import sys

T = int(input().strip())
for _ in range(T):
    n , k = map(int , input().split())
    print(k-1 if ((k-1) | k) <= n else k-2)