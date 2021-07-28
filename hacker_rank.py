#!/bin/python3

import math
import os
import random
import re
import sys



def calculate_health(d,first,last):
    # print(genes)
    # print(health)
    
    d += "0"
    sum = 0
    
    for i in range(0,len(d)-1):
        if (d[i] == d[i+1]):
            temp = d[i]+d[i+1]
            if temp in genes:
               
                if first <= genes.index(temp) <= last:
                    # print("inde=>"+str(genes.index(temp)))
                    # print(health[genes.index(temp)])
                    sum += health[genes.index(temp)]
                
        else:
            # print("d->"+str(d[i]))
            # list1 = [ genes.index(data) for data in genes if d[i] == data ]
            list1 = [ k for k in range(len(genes)) if genes[k] == d[i] ]
            for list1_ele in list1:
                if first <= list1_ele <= last:
                    # print(health[list1_ele])
                    sum += health[list1_ele]
    
    dna_list.append(sum)

    return dna_list
            


if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))
    
    dna_list = []

    s = int(input().strip())

    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]
        
        h = calculate_health(d,first,last)
        
    print(min(h), max(h))
