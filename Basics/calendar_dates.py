#
#

class Date:
    
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.day = init_day
        self.month = init_month
        self.year = init_year
        
        
        
        
        
        
        
        
        

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

#### Put your code for problem 2 below. ####


    def advance_one(self):
        
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.is_leap_year() == True:
            
            days_in_month[2] = 29
            
        if days_in_month[self.month] == 31 and self.month == 12 and self.day == 31:
            
            self.day = 1
            
            self.month = 1
            
            self.year += 1
            
        elif days_in_month[self.month] == 31 and self.day == 31:
            
            self.day = 1
            
            self.month += 1
            
        elif days_in_month[self.month] == 30 and self.day == 30:
            
            self.day = 1
            
            self.month += 1
            
        elif days_in_month[self.month] == 28 and self.day == 28:
        
            self.day = 1
            
            self.month += 1
        
        elif days_in_month[self.month] == 29 and self.day == 29:
        
            self.day = 1
            
            self.month += 1
        
        else: 
            
            self.day += 1
            
            
    def advance_n(self,n):
        
        print(self)
        
        for x in range(n):
            
            self.advance_one()
            
            print(self)
     
        
    def __eq__(self,other):
         
         if self.day == other.day and self.month == other.month and self.year == other.year:
             
             
             return True
            
            
    def is_before(self, other):
        
        if self.year < other.year:
            
            return True
        
        elif self.month < other.month and self.year <= other.year:
            
            return True
        
        elif self.day < other.day and self.month <= other.month and self.year <= other.year:
        
            return True
        
        else:
        
            return False



    def is_after(self,other):
        
        
        if other.is_before(self) == True:
            
            return True
                
        else:
            
            return False


    def days_between(self,other):
        
        first_date = other.copy()
        
        second_date = self.copy()
        
        #determines if the self comes before other or not 
   

        after = second_date.is_after(first_date)
        
        if first_date.day == second_date.day and first_date.month == second_date.month and first_date.year == second_date.year:
            
            return 0

        if after == True:

           count = 0 
            
           while True:
                
                if first_date.day == second_date.day and first_date.month == second_date.month and first_date.year == second_date.year:                   
                    
                    break
                
                first_date.advance_one()
                
                count += 1
                
        else:     
            
        
            return first_date.days_between(second_date)*-1
        
      
        return count 
    
    
    def day_name(self):
        
        known_date = Date(11,11,2019)
        
        day_names = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        number_of_days = self.days_between(known_date)
        
        day = number_of_days % 7 
        
        return day_names[day]
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            
