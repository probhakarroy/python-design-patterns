import abc


class Director:
    """Director"""

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()


    def get_car(self):
        return self._builder.car


class Builder(abc.ABC):
    """Abstract Builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkylarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts"""

    # Methods to be used by the Director class
    def add_model(self):
        self.car.model = 'Skylark'

    def add_tires(self):
        self.car.tires = 'Regular tires'

    def add_engine(self):
        self.car.engine = 'Turbo engine'


class Car():
    """Product"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


if __name__ == "__main__":
    # instantiate the concrete builder
    builder = SkylarkBuilder()
    
    # construct car using the Director
    director = Director(builder)
    director.construct_car()
    car = director.get_car()
    print(car)