#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:19:17 2019

@author: Farid
"""


class Board:
    
    
    def __init__(self, height, width):
        
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def __repr__(self):
            """ Returns a string representation for a Board object.
            """
            s = ''         # begin with an empty string

    # add one row of slots at a time
            for row in range(self.height):
                s += '|'   # one vertical bar at the start of the row

                for col in range(self.width):
                    s += self.slots[row][col] + '|'

                s += '\n'  # newline at the end of the row

    # Add code here for the hyphens at the bottom of the board
    # and the numbers underneath it.
                
                
            s += '-'* ((self.width*2)+1)
            s+= '\n'
                
                
            for x in range(self.width):
                    
                    s += " " + str(x)
                   
                    
            
            return s


    def add_checker(self, checker, col):
        
        """ put your docstring here
    """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

    
        row = self.height - 1 
        
        while self.slots[row][col] != ' ':
            
            row -= 1
            
            if row < 0:
                
                break
        
        if row < 0:
            
            self.slots[self.height - 1][col] = checker
        
        else: 
            self.slots[row][col] = checker
           
        
    def reset(self):
            
           for row in range(self.height):
               
               for col in range(self.width):
                   
                   self.slots[row][col] = " "
                   
                   
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                        self.add_checker(checker, col)

        # switch to the other checker
            if checker == 'X':
                        checker = 'O'
            else:
                        checker = 'X'               
                
    def can_add_to(self, col):
            
            if col < 0 or col > self.width - 1:
                
                return False
        
        
            if self.slots[0][col] != " ":
                
                return False
           
            
            else: 
                return True
            
            
    def is_full(self):
        
        for col in range(self.width):
            
            x = self.can_add_to(col)
            
            if x == True:
                
                break
            
            
        if x == True:
            
            return False
        
        else: 
            
            return True
        
    def remove_checker(self, col): 
            
           for row in range(self.height):
               
               if self.slots[row][col] == "X" or self.slots[row][col] == "O":
                   
                   self.slots[row][col] = " "
                   
                   break

        
   #helper functions for is_win_for
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                self.slots[row][col + 1] == checker and \
                self.slots[row][col + 2] == checker and \
                self.slots[row][col + 3] == checker:
                    return True

    # if we make it here, there were no horizontal wins
        return False
   
    def is_vertical_win(self,checker):
        
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                self.slots[row+1][col] == checker and \
                self.slots[row+2][col] == checker and \
                self.slots[row+3][col] == checker:
                    return True

        return False
       
       
    def is_up_diagonal_win(self,checker):
         
         for row in range(self.height//2, self.height):
            for col in range(self.width//2):
                if self.slots[row][col] == checker and \
                self.slots[row-1][col+1] == checker and \
                self.slots[row-2][col+2] == checker and \
                self.slots[row-3][col+3] == checker:
                    return True

         return False
    
    def is_down_diagonal_win(self,checker):
        
         for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                self.slots[row+1][col+1] == checker and \
                self.slots[row+2][col+2] == checker and \
                self.slots[row+3][col+3] == checker:
                    return True

         return False
    
    
    
    def is_win_for(self, checker):
        
        """ put your docstring here
        """
        assert(checker == 'X' or checker == 'O')

        # call the helper functions and use their return values to
        # determine whether to return True or False
        
        
        if self.is_vertical_win(checker) == True or \
           self.is_horizontal_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True:
               
              return True
          
        else:
            
              return False
        
        
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        