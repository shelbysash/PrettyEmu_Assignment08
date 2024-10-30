#roman py

# Name: Roman Stryjewski
# email:  stryjerj@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   10/31/24
# Course #/Section:   IS 4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Creating code for to create classes we are passionate about and put them together into a main modules

# Brief Description of what this module does. My module about halloween with the class CarvingPumpkins
# Citations:
# Anything else that's relevant:

class CarvingPumpkin:
    def __init__(self, pattern, light):
        self._pattern = pattern
        self._light = light

    #defines the pattern property
    def pattern(self):
        return self._pattern

    #the setter for the pattern property
    def pattern(self, value):
        self._pattern = value

    #defines the light property
    def light(self):
        return self._light

    #the setter for the light property
    def light(self, value):
        self._light = value

    def carve(self, pattern):
        self.pattern = pattern
        print("The pumpkin is carved into a ", self.pattern)

    def turn_on(self):
        self.light = "on"
        print("The pumpkin light is now ", self.light)

    def turn_off(self):
        self.light = "off"
        print("The pumpkin light is now " , self.light)

    def __str__(self):
        return ("Carving Pumpkin with pattern: ", self.pattern , "Light= " , self.light)

    def __repr__(self):
        return ("CarvingPumpkin(pattern= " , self.pattern , "light= " , self.light)






    #if __name__ == "__main__":
    #pumpkin = CarvingPumpkin("scary face", "off")
    #print(pumpkin)
    #pumpkin.carve("happy face")
    #pumpkin.turn_on()
    #pumpkin.turn_off()
