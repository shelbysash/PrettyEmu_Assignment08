#Sidney.py

# Name: Sidney Huschart
# email:  huschash@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   October 31, 2024
# Course #/Section:   IS4010-001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  working as a team to collaborate using github to display our knowlegd of classes. 

# Brief Description of what this module does:   demonstrates our knowledge of classes and how to use them. 
# Citations:
# Anything else that's relevant:

class ChristmasCookies(object):
    """
    Model a Christmas cookie that can be made during December. 
    """
    def __init__(self, type):  #__init__
        """
        Constructor
        @param type String: The type of cookie
        
        """
        self.__type = type

    def get_type(self): #getter
        """
        @return String: The cookie type of the current object
        """
        return self.__type
    
    def set_type(self, type): #setter
        """
        Assign a value to the cookie type of the current object
        @param type String: The cookie type to be assigned.
        """
        self.__type = type
        
    def print_type(self):  #class that does something-- this will print something
        """
        Print the cookie type of the current object
        """
        print(self.__type)
        
    def __str__(self):  #__str__
        """
        @return String: A human-readable basic representation of the current object. 
        Useful for debugging, documentation, etc.
        """
        return "type: " + self.__type

    def __repr__(self): #__repr__ 
        """
        @return String: A string containing code that can be executed to create a copy of the current object
        """
        return f"ChristmasCookies('{self.__type}')"
    
