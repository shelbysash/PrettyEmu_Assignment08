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
        
    """
    def __init__(self, type):
        """
        Constructor (duh)
        @param type String: The type of cookie
        
        """
        self.__type = type

    def get_type(self):
        """
        @return String: The  type of the current object
        """
        return self.__type
    
    def set_type(self, type):
        """
        Assign a value to the vehicle type of the current object
        @param type String: The vehicle type to be assigned.
        """
        self.__type = type
        
    def print_type(self):
        """
        Print the vehicle type of the current object
        """
        print(self.__type)
        
    def __str__(self):
        """
        @return String: A human-readable basic representation of the current object. 
        Useful for debugging, documentation, etc.
        """
        return "type: " + self.__type

    def __repr__(self):
        """
        @return String: A string containing code that can be executed to create a copy of the current object
        """
        return f"Vehicle('{self.__type}')"
    
if __name__ == "__main__":
    print("Vehicle class test logic...")
    car = Vehicle("Corvette")
    print("Type attribute of Vehicle object:", car.get_type())
    print("Changing the type of the object...")
    car.set_type("GTO")
    print("Type attribute of Vehicle object:", car.get_type())

    print("\n\nTesting the repr method...")

    print("From __repr__():", car.__repr__())
    carCopy = eval(car.__repr__())
    print("Copied car:", carCopy.__str__())

    print("Type attribute of original Vehicle object:", car.get_type())
    print("Type attribute of copied Vehicle object:", carCopy.get_type())
