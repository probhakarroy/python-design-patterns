class House:  # The class being visited
    def accept(self, visitor):
        """Interface to accept a visitor"""
        # Trigger the visiting operation
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        # Note that we now have a reference to the HVAC specialist object in the house object!
        print(self, 'worked on by', hvac_specialist)

    def work_on_electricity(self, electrician):
        # Note that we now have a reference to the electrician object in the house object!
        print(self, 'worked on by', electrician)

    def __str__(self):
        """Simply return the class name when House object is printed"""
        return self.__class__.__name__


class Visitor:
    """Abstract visitor"""

    def __str__(self):
        """Simply return the class name when Visitor object is printed"""
        return self.__class__.__name__


class HvacSpecialist(Visitor):  # Inherits from the parent class, Visitor
    """Concrete visitor: HVAC specialist"""

    def visit(self, house):
        # Note that visitor now has a reference to the house object!
        house.work_on_hvac(self)


class Electrician(Visitor):  # Inherits from the parent class, Visitor
    """Concrete visitor: electrician"""

    def visit(self, house):
        # Note that visitor now has a reference to the house object!
        house.work_on_electricity(self)


if __name__ == "__main__":
    # Create an HVAC specialist
    hv = HvacSpecialist()

    # Create an Electrician
    e = Electrician()

    # Create a house
    house = House()

    # Let the house accept the HVAC specialist and work on the house by invoking the visit() method
    house.accept(hv)

    house.accept(e)
