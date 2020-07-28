import types


class Strategy:
    """The Strategy pattern class"""

    def __init__(self, function=None):
        self.name = 'Default Strategy'

        # If a reference to a function is provided, replace the execute() method with the given function
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):  # This gets replaced by another version, if another strategy is provided
        """Default method that prints the name of the strategy being used"""
        print(f'{self.name} is being used!')


# Replacement method 1
def strategy_one(self):
    print(f'{self.name} is used to execute method 1')


# Replacement method 2
def strategy_two(self):
    print(f'{self.name} is used to execute method 2')


# Let's create our default Strategy
s0 = Strategy()
# Let's execute our default strategy
s0.execute()

# Let's create the first variation of our default strategy by providing a new behavior
s1 = Strategy(strategy_one)
# Let's set its name
s1.name = 'Strategy One'
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = 'Strategy Two'
s2.execute()
