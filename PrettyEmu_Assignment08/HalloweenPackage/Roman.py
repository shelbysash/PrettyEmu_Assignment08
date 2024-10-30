# Name: Roman Stryjewski
# email:  stryjerj@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   10/31/24
# Course #/Section:   IS 4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment: Creating code for to create classes we are passionate about and put them together into a main modules
# Brief Description of what this module does. My module about halloween with the class CarvingPumpkins
# Citations: n/a
# Anything else that's relevant: n/a

#roman py

class HalloweenCarvingPumpkin:
    """
    Model a pumpkin-related activity to celebrate Halloween
    """
    def __init__(self, type):  #__init__
        """
        Constructor
        @param type String: The type of cookie
        
        """
        self.__type = type
        
    def get_type(self): #getter
        """
        @return String: The halloween activity type of the current object
        """
        return self.__type
    
    def set_type(self, type): #setter
        """
        Assign a value to the halloween activity type of the current object
        @param type String: The cookie type to be assigned.
        """
        self.__type = type
        
    def set_type(self, type): #setter
        """
        Assign a value to the halloween activity type of the current object
        @param type String: The halloween activity type to be assigned.
        """
        self.__type = type
        
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
        return f"HalloweenCarvingPumpkin('{self.__type}')"
    




   



    #if __name__ == "__main__":
    #pumpkin = CarvingPumpkin("scary face", "off")
    #print(pumpkin)
    #pumpkin.carve("happy face")
    #pumpkin.turn_on()
    #pumpkin.turn_off()
