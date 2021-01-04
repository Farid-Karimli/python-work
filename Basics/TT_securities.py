#
#
# TT Securities    
#
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
def avg_price(prices):
    """ computes the average of the values in the list prices
    """
    
    
    
    
    avg = 0 
    
    for x in prices: 
        
        avg = avg + x
        
        
    return avg/len(prices)
    

def std_dev(prices):
    """computes the standard deviation of the values in the list prices
    """
    
    
    avg = avg_price(prices)
    
    numerator = 0
    
    for x in prices:
        
        numerator = numerator + (x - avg)**2
        
    deviation = math.sqrt(numerator/len(prices))
    
    return deviation

def max_day(prices):
    """ returns the day of the maximum price
    """
    
    
    day = 0
    
    for x in range(len(prices)):
        
        if prices[x] > prices[x-1] and prices[x] > prices[day]:
            
            day = x 
        
    return day



def max_price(prices):
    """ returns the mximum price - this is a helper function
    """
    
    maximum = prices[0]
    
    for x in range(len(prices)):
        
        if prices[x] > prices[x-1] and prices[x] > maximum:
            
            maximum = prices[x] 
        
    return maximum
        
def any_below(prices,threshold):
    """ return True if a value in prices is smaller than the value threshold
    """
    
    
    
    for x in prices:
        
        if x < threshold:
            
            return True
        
    return False
    
def find_plan(prices):
    """ returns the best day to buy and the best day to sell a product as well 
    returns the proit
    """
    
    
    
    buy = 0
    
    sell = 0
    
    profit = 0
    
    max_diff = prices[0] - prices[-1]
    
    for x in range(len(prices)):
        
        for y in range(len(prices)):
            
            diff = abs(prices[x] - prices[y])
            
            if diff > max_diff and y > x and prices[x] < prices[y]:
                    
                max_diff = diff
                    
                buy = x
                

                sell = y
                

                profit = diff
                    
    return [buy,sell,profit]










def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            
          print(avg_price(prices))
        
        elif choice == 4:
            
          print(std_dev(prices))
        
        elif choice == 5:
        
          day_price =  max_day(prices)
        
          maximum_price = max_price(prices)
        
          print("The max price is", maximum_price, "on day", day_price)
        
        elif choice == 6:
            
            threshold = int(input("Enter the threshold: "))
            
            answer = any_below(prices, threshold)
            
            
            if answer == True:
                
                print("There is at least one price below",threshold)
                    
            else: 
                
                print("There are no prices below",threshold)
        
        elif choice == 7:
            
            plan = find_plan(prices)
            
            buy_price = 0
            
            sell_price = 0
            
            for x in range(len(prices)):
                
                if x == plan[0]:
                    
                    buy_price = prices[x]
                    
                    
                elif x == plan[1]:
                    
                    sell_price = prices[x]
            
            print("Buy on day",plan[0],"at price",buy_price)
            print("Sell on day",plan[1],"at price",sell_price)
            print("Total proit:",plan[2])
        
        
       
            
            
            
            
            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
