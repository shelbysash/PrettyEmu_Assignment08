# Name: Shelby Sash
# email: sashsk@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: October 31,2024
# Course #/Section: IS4010/ 001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Collaborate with a group to practice OOP principles and architecture
# Brief Description of what this module does: Entry point for the project  
# Citations: N/A
# Anything else that's relevant: N/A

#main.py
#shelby 

from ChristmasPackage.Sidney import *
from HalloweenPackage.Roman import *
from EidPackage.Cheikh import *

if __name__ == "__main__":
    print("We modeled activities and/or deserts we enjoy with our favorite holidays:")
    print(" ")
    #Sidney's Christmas Cookie functionality tests
    print("Sidney's Christmas Cookies class test logic...")
    cookie = ChristmasCookies("Sugar Cookie")  
    print("Type attribute of Christmas Cookie object:", cookie.get_type()) 
    print("Changing the type of the object...")
    cookie.set_type("Frosted Sugar Cookie")
    print("Type attribute of Christmas Cookie object:", cookie.get_type())
    print("Testing the repr method...")
    print("From __repr__():", cookie.__repr__())
    cookieCopy = eval(cookie.__repr__())
    print("Copied cookie:", cookieCopy.__str__())
    print("Type attribute of original Christmas Cookie object:", cookie.get_type())
    print("Type attribute of copied Christmas Cookie object:", cookieCopy.get_type())

    print(" ")
    print(" ")
    print(" ")
    #Cheikh's Eid Celebration functionality tests
    print("Cheikh's Eid Celebration class test logic...")
    firstActivity = EidCelebration("Sharing gifts")  
    print("Type attribute of first activity object:", firstActivity.get_type()) 
    print("Changing the type of the object...")
    firstActivity.set_type("Cooking senegalese cuisine")
    print("Type attribute of the first activity object:", firstActivity.get_type())
    print("Testing the repr method...")
    print("From __repr__():", firstActivity.__repr__())
    firstActivityCopy = eval(firstActivity.__repr__())
    print("Copied first activity:", firstActivityCopy.__str__())
    print("Type attribute of original Eid Celebration object:", firstActivity.get_type())
    print("Type attribute of copied Eid Celebration object:", firstActivityCopy.get_type())

    print(" ")
    print(" ")
    print(" ")
    #Roman's Eid Halloween pumpkin carving functionality tests
    print("Roman's Halloween Carving Pumpkin class test logic...")
    HalloweenActivity = HalloweenCarvingPumpkin("Carving Pumpkins")  
    print("Type attribute of halloween activity object:", HalloweenActivity.get_type()) 
    print("Changing the type of the object...")
    HalloweenActivity.set_type("Painting Pumpkins")
    print("Type attribute of the Halloween Activity object:", HalloweenActivity.get_type())
    print("Testing the repr method...")
    print("From __repr__():", HalloweenActivity.__repr__())
    HalloweenActivityCopy = eval(HalloweenActivity.__repr__())
    print("Copied Halloween Activity:", HalloweenActivityCopy.__str__())
    print("Type attribute of original Halloween Pumpkin Carving object:", HalloweenActivity.get_type())
    print("Type attribute of copied Halloween Carving Pumpkin object:", HalloweenActivityCopy.get_type())