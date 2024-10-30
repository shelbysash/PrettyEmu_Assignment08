# *****************************************************
# Name: Cheikh Abdoul
# email:  abdoulch@mail.uc.edu
# Assignment Number: Assignment08
# Due Date:   10/31/2024
# Course #/Section:   001
# Semester/Year:   fall 2024
# Brief Description of the assignment: Group project of topics that interested us using __init__ , __str__, and __repr__ methods for the classes.
# Brief Citations: N/A
# Anything else that's relevant:
# *****************************************************
# cheikh py

class EidCelebration:
    """
    Model different activities to celebrate the holiday Eid
    """
    def __init__(self, type): #__init_
        """
        Constructor
        @param type String: The type of activity
        """
        self._type = type
    def get_type(self): #getter
        """
        @return String: The activity type of the current object return self.-type
        """
    def set_type(self, type): #setter
        """
        Assign a value to the activity type of the current object 
        @param type String: The activity type to be assigned.
        """
        self .__type = type

    def print_type(self):
        """
        Print the activity type of the current object
        """
        print (self.__type)

    def __str__(self): #__str_
        """
        @return String: A human-readable basic representation of the current object.
        Useful for debugging, documentation, etc.
        """
        return "type:" + self.__type

    def __repr__(self): # repr_
        """
        return String: A string containing code that can be executed to create a copy of the current object
        """
        return f"EidCelebration('{self.__type}')"


