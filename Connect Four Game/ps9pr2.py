#
# ps9pr2.py  (Problem Set 9, Problem 2)
#ps9pr2.py
# A Connect-Four Player class 

from ps9pr1 import Board

# write your class below

class Player:
    
    def __init__(self,checker):
        
        assert(checker == 'X' or checker == "O")

        
        self.checker = checker
        
        self.num_moves = 0
        
        
        
    def __repr__(self):
        
        if self.checker == "X":
        
            return "Player X"
        
        else: 
        
            return "Player O"
        
    def opponent_checker(self):
        
        if self.checker == "X":
        
            return "O"
        
        else: 
        
            return 'X'
        
        
    def next_move(self,b):
        
         self.num_moves += 1
            
         while True:
                 
                 col = int(input('Enter a column: '))

                 
                 if b.can_add_to(col) == True: 
                    
                    return col
                
                    break
                
                
                 print("Try Again!")
                 