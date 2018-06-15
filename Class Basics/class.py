"""
This is a program to illustrate the basics of Object Oriented concepts in Python
"""
class vehicle:
    def general_usage(self):
        print("General Use: Transportation")

class car(vehicle):
    def __init__(self, n='Car', m='Make'):
        self.name = n
        self.make = m

    def specific_usage(self):
        print("Specific usage is for Family Trips")

class bike(vehicle):
    def __init__(self, n='Bike', m='Make'):
        self.name = n
        self.make = m

    def specific_usage(self):
        print("Specific usage is for Short movements")

c = car('Mycar','Hyundai')

print("My Cars name is ",c.name)
print("My Cars Make is ",c.make)
c.general_usage()
c.specific_usage()

