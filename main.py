# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

#


class Podracer:

    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    # Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"


# Define a new class, AnakinsPod that inherits the Podracer class.


class AnakinsPod(Podracer):

    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    # but also contains a special method called boost that will multiply max_speed by 2.
    def boost(self):
        self.max_speed *= 2


# Define another class that inherits Podracer and call this one SebulbasPod.
class SebulbasPod(Podracer):

    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)


#This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

    def flame_jet(self, other):
        other.condition = "trashed"
