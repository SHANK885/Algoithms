# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# find length of the longest common subsequece for two strings X and Y
#import math
import numpy as np

def LCS(str1, str2):
    m = len(str1)
    n = len(str2)
    #print("m = {}, n = {}".format(m, n))
    C = np.zeros((len(X)+1, len(Y)+1))

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                #print("inside if")
                C[i,j] = C[i-1, j-1] + 1
            else:
                #print("inside else")
                C[i,j] = max(C[i-1, j], C[i, j-1])
    
    return C


if __name__ == "__main__":
    
    X = "ABCDEFGHIJ"
    Y = "ABBCCDDEEF"
    
    arr = LCS(X,Y)
    
    print("Length of longest common subsequence: ", arr[-1,-1])