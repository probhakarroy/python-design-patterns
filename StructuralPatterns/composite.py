import abc


class Component(abc.ABC):
    """Abstract class"""

    @abc.abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    # Our interface method
    @abc.abstractmethod
    def component_function(self):
        pass


class Child(Component):  # Inherits from the abstract class, Component
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # These is where we store the name of your child items!
        self.name = args[0]

    def component_function(self):
        # print the name of your child object here!
        print(self.name)


class Composite(Component):  # Inherits from the abstract class, Component
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # These is where we'll store the name of the composite objects
        self.name = args[0]

        # These is where we keep our child items
        self.children = []

    def append_child(self, child):
        """Method to add a new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Method to remove a child item"""
        self.children.remove(child)

    def component_function(self):
        # print the name of the composite object
        print(self.name)

        # Iterate through the child objects and invoke their component_function printing their names
        for i in self.children:
            i.component_function()


if __name__ == "__main__":
    # Build a Composite Submenu 1
    sub1 = Composite('submenu1')

    # Create a new child sub_submenu_11
    sub11 = Child('sub_submenu_11')

    # Create a new child sub_submenu_12
    sub12 = Child('sub_submenu_12')

    # Add the sub_submenu 11 to submenu 1
    sub1.append_child(sub11)

    # Add the sub_submenu 12 to submenu 1
    sub1.append_child(sub12)

    # Build a top-level Composite Menu
    top = Composite('top_menu')

    # Build a submenu 2 that is not a composite
    sub2 = Child('submenu2')

    # Add the submenu_1 & submenu_2 to top_menu
    top.append_child(sub1)
    top.append_child(sub2)

    # Let's test if our Composite pattern works or not!
    top.component_function()
