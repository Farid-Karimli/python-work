#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the Player class or a subclass of Player).
          One player should use 'X' checkers and the other should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b





def process_move(p,b):
    """processes a move for player p and board b
    """
    
    
    print("Player "+ p.checker + "'s " + "Turn")
    
    x = p.next_move(b)
    
    b.add_checker(p.checker,x)
    
    print("\n")
    
    print(b)
    
    print("\n")
    
    if b.is_win_for('X') ==  b.is_win_for('O') == True:
        
        print("It's a tie")
        
        return True
    
    elif b.is_win_for('X') == True:
        
        print("Player X wins in " + str(p.num_moves) + " moves. Congratulations!")
        
        return True
    elif b.is_win_for('O') == True:
        
        print("Player O wins in " + str(p.num_moves) + " moves. Congratulations!")
        
        return True
    
    else: 
        
        return False
    
    
    
class RandomPlayer(Player):
    """ used for an unintelligent computer player that chooses at random from the available columns.
    """
    
    
    def next_move(self,b):
    
        self.num_moves += 1
        
        lst_col = []
        
        for col in range(b.width):
            
            if b.can_add_to(col) == True: 
                
                lst_col += [col]
                
                
            
        random_column = random.choice(lst_col)


        return random_column
            
        
            
            
            
        
   
        
        
    
    
    
    
    
    
    
    

    

































