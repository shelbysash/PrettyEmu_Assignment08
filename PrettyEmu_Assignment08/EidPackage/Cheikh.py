# *****************************************************
# Name: Cheikh Abdoul
# email:  abdoulch@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   10/31/2024
# Course #/Section: IS 4010 001
# Semester/Year:   fall 2024
# Brief Description of the assignment: Group project of topics that interested us using __init__ , __str__, and __repr__ methods for the classes.
# Brief Description of what this module does: Models the Eid Celebration class
# Brief Citations: N/A
# Anything else that's relevant: N/A
# *****************************************************
# cheikh py

class EidCelebration:
    """
    Model different activities to celebrate the holiday Eid 
    """
    def __init__(self, type):  #__init__
        """
        Constructor
        @param type String: The type of activity
        
        """
        self.__type = type

    def get_type(self): #getter
        """
        @return String: The activity type of the current object
        """
        return self.__type
    
    def set_type(self, type): #setter
        """
        Assign a value to the activity type of the current object
        @param type String: The activity type to be assigned.
        """
        self.__type = type

    def print_type(self):  #class that does something-- this will print something
        """
        Print the activity type of the current object
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
        return f"EidCelebration('{self.__type}')"






 

