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
    def __init__(self, celebration_name, family_gathering, gift_price):
        self.celebration_name = celebration_name
        self.family_gathering = family_gathering  
        self._gift_price = gift_price  

    def __str__(self):
        return f"Celebration_name = {self.celebration_name}, family_gathering = {self.family_gathering}, gift_price = {self._gift_price})"

    def __repr__(self):
        return f"{self.celebration_name}, {self.family_gathering}, {self._gift_price}"

    @property
    def gift_price(self):
        return self._gift_price

    @gift_price.setter
    def gift_budget(self, value):
        if value >= 0:
            self._gift_price = value
        else:
            print("Price of gift can't be negative.")

    def prepare_meal(self):
        """
        Preparing a meal for the Eid celebration
        """
        return "The Eid lunch is being prepared with traditional senegalese cuisine."

    def share_gift(self):
        """
        Sharing gifts with family members
        """
        if self.family_gathering:
            return f"Gift is shared with a price tag of ${self._gift_price}!"
        else:
            return "Gift is not being shared."

    def turn_on_lightsandmusic(self):
        """
        Turning on celebration lights for Eid
        """
        return "Lights and music have been turned on for Eid."


