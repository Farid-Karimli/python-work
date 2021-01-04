#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:06:43 2019

@author: Farid
"""

alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"


alph = alphabet.split(" ")


def vigenere_cipher():
    
    message = input("Enter message: ")
    
    key = input("Enter key: ")
    
    
    # index1 = alph.index()
    result = ""
     
    
    
    for x in range(len(message)):
        
        
        index1 = alph.index(message[x])
    
        index2 = alph.index(key[x])
        
        new_letter = alph[(index1 +index2)%26]     
        
        result += new_letter
        
        
        
        
        
    return result
    
    
    
    
    
    
    
    
    
    
    
