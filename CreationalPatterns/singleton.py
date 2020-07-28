class Borg:
    """Borg class making class attributes global"""
    _shared_state = {}  # Attribute Dictionary

    def __init__(self):
        self.__dict__ = self._shared_state  # Make it an attribute dictionary


class Singleton(Borg):  # inherits from Borg class
    """This class now shares all its attributes among all its various instances"""
    # This essentially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)    # super().__init__() --> same
        # update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state)


# Let's create a singleton object and add our first acronym
x = Singleton(HTTP='Hyper Text Transfer Protocol')

# Print the object
print(x)

# Let's create another singleton object and if it refers to the same attribute
y = Singleton(SNMP='Single Network Management Protocol')

print(y)
