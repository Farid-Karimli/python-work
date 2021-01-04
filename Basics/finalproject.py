#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:37:33 2019

@author: Farid
"""
def clean_text(txt):
    
    s = txt.lower()
    
    s = s.replace('.','')
    
    s = s.replace(',', '')
    
    s = s.replace('?','')

    s = s.replace('!','')
    
    s = s.split(" ")

    return s

def sample_file_write(filename):
        """A function that demonstrates how to write a
           Python dictionary to an easily-readable file.
        """
        d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
        f = open(filename, 'w')      # Open file for writing.
        f.write(str(d))              # Writes the dictionary to the file.
        f.close()                    # Close the file.
            
            
        
def sample_file_read(filename):
         """A function that demonstrates how to read a
         Python dictionary from a file.
         """
         f = open(filename, 'r')    # Open for reading.
         d_str = f.read()           # Read in a string that represents a dict.
         f.close()

         d = dict(eval(d_str))      # Convert the string to a dictionary.

         print("Inside the newly-read dictionary, d, we have:")
         print(d)
        
        


class TextModel:
    
    def __init__(self, model_name):
        
        self.name = model_name
        
        self.words = {}
        
        self.word_lengths = {}
        
    def __repr__(self):
        """Return a string representation of the TextModel."""
        
        s = 'text model name: ' + self.name + '\n'
       
        s += '  number of words: ' + str(len(self.words)) + '\n'
        
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        
        return s
    
    
    def add_string(self, s):
        
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.
        """
            
        word_list = clean_text(s)
        
        
        for w in word_list:
            
            if w in self.words:
                
                self.words[w] += 1
                
            else:
                
                self.words[w] = 1
                
                
        for w in word_list:
            
            if len(w) in self.word_lengths:
                
                self.word_lengths[len(w)] += 1
                
            else:
                
                self.word_lengths[len(w)] = 1 
                
        
        
    def add_file(self,filename):
        
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        f.close()
        
        
        words = clean_text(text)
        
        self.add_string(words)


    def save_model(self):
        
        d1 = self.words
        
        f1 = open(self.name + "_words", 'w')
        
        f1.write(str(d1))
        
        f1.close()
        
        d2 = self.word_lengths
        
        f2 = open(self.name + '_word_lengths', 'w')
        
        f2.write(str(d2))
        
        
        
    def read_model(self):
        
        
        f1 = open(self.name + "_words", 'r')
        d_read = f1.read()
        f1.close()

        self.words = dict(eval(d_read))
        
        
        
        f2 = open(self.name + "_word_lengths", 'r')
        d2_read = f2.read()
        f2.close()
        
        self.word_lengths = dict(eval(d2_read))
        
        
        
        
        
        
        
        
        