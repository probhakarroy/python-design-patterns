class Subject:  # Represents what is being 'observed'
    def __init__(self):
        self._observers = []  # This where references to all the observers are being kept
        # Note that this is a one-to-many relationship: there will be one subject to be observed by many _observers

    def attach(self, observer):
        if observer not in self._observers:     # If the observer is not already in the observers list
            # append the observer to the list
            self._observers.append(observer)

    def detach(self, observer):  # Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:    # for all the observers in the list
            if modifier != observer:        # Don't notify the observer who is actually updating the temperature
                # Alert the observer ... update method needs a subject hence the subject instance is passed here.
                observer.update(self)


class Core(Subject):  # Inherits from the Subject class
    def __init__(self, name=''):
        Subject.__init__(self)
        self._name = name  # Set the name of the core
        self._temp = 0  # Initialize the temperature of the core

    @property  # Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter  # Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        self.notify()   # Notify the observers whenever somebody changes the core temperature


class TempViewer:
    """Observer class"""

    def update(self, subject):  # Alert method that is invoked when the notify() method in a concrete subject is invoked
        print(
            f'Temperature Viewer: {subject._name} has Temperature: {subject._temp}')


if __name__ == "__main__":
    # Let's create our subjects
    c1 = Core('Core 1')
    c2 = Core('Core 2')

    # Let's create our observers
    v1 = TempViewer()
    v2 = TempViewer()

    # Let's attach our observers to the first core
    c1.attach(v1)
    c1.attach(v2)

    # Let's change the temperature of the first core
    c1.temp = 80
    c1.temp = 90
