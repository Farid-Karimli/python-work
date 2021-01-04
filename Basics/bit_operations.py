#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:00:11 2019

@author: Farid
"""

def bitwise_and(b1,b2):
    """ 
    takes two binary numbers,  ANDed together each pair of corresponding bits to produce the appropriate bit for the result.
    """
   
    if b1 == "" and b2 == "":
    
        return ""
    
    elif b1 == "":
        
        return "0"*len(b2)
    
    elif b2 == "":
        
        return "0"*len(b1)
     
        
    else: 
        
        rest = bitwise_and(b1[:-1],b2[:-1])
        
        if len(b1) == len(b2):
        
            if b1[-1] == "0" and b2[-1] == "0":
            
                return rest + "0"
        
            elif b1[-1] == "1" and b2[-1] == "1":
        
                return rest + "1"
        
            else: 
            
                return rest + "0"
    
        elif len(b1) > len(b2):
            
            b2_with_zeroes = "0"*(len(b1) - len(b2)) + b2
        
            return bitwise_and(b1,b2_with_zeroes) 
       
        
        elif len(b2) > len(b1):
            
            b1_with_zeroes = "0"*(len(b2) - len(b1)) + b1
            
            return bitwise_and(b1_with_zeroes,b2) 
        
        

def add_bitwise(b1,b2):
    """ 
    adds two binary numbers without any conversion
    """
    
    
    
    
    
    if b1 == "":
        
        return b2
    
    elif b2 == "":
    
        return b1
    
    elif b1 == "" and b2 == "":
        
        return ""
    
    elif b1 == "1" and b2 == "1":
    
        return "10"
    
    else: 
        
        rest = add_bitwise(b1[:-1],b2[:-1])
        
        if len(b1) == len(b2): 
            
            if b1[-1] == "0" and b2[-1] == "0":
        
                return rest + "0"
        
            elif b1[-1] == "1" and b2[-1] == "0":
            
                return rest + "1"
        
            elif b1[-1] == "0" and b2[-1] == "1":
        
                return rest + "1"
        
        
            elif b1[-1] == "1" and b2[-1] == "1" and len(b1) != 1 and len(b2) != 1:
            
                rest = add_bitwise(b1[:-1],b2[:-1])
            
                if rest == "10":
            
                    rest = "11" 
    
                elif rest == "":
        
                    rest = "10"
            
                elif rest == "1":
                
                    rest = "10"
            
                else: 
                
                    return "1" + rest 
            
                return rest + "0"
        
        
        elif len(b1) > len(b2):
            
            b2_with_zeroes = "0"*(len(b1) - len(b2)) + b2
        
            return add_bitwise(b1,b2_with_zeroes) 
       
        
        elif len(b2) > len(b1):
            
            b1_with_zeroes = "0"*(len(b2) - len(b1)) + b1
            
            return add_bitwise(b1_with_zeroes,b2) 
        
        
        
        
        
        
        
        
        
       



























