#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 22:44:30 2021

@author: johnsenaakoto
"""

#power_hungry

def solution(xs):
    #   This function finds the maximum product of a subset from the input set
    
    if len(xs) == 1 and xs[0] < 0:
        return(str(xs[0]))
    
    #   creates a list for positive numbers and negative numbers
    positives = [num for num in xs if num > 0]
    negatives = [num for num in xs if num < 0]
    
    
    
    if (len(negatives) % 2) != 0:
        negatives.sort()
        del negatives[-1]
        
    if len(negatives) or len(positives):
        product = 1
        
        for multiplier in negatives + positives:
            product *= multiplier
            
        return(str(product))
    
    return('0')

print(solution([ -4]))
