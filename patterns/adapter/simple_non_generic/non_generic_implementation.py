""" 
This works, but if we need to Adapt more classes, then we're going to need to write an adapter
for each one.  See second implementation for a generic way to do this
"""
class Person(object):
    """A representation of a person in 2D Land"""
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        return "hello"

class DogAdapter(object):
    """Adapts the Dog class through encapsulation"""
    def __init__(self, canine):
        self.canine = canine

    def make_noise(self):
        """This is the only method that's adapted"""
        return self.canine.bark()

    def __getattr__(self, attr):
        """Everything else is delegated to the object"""
        return getattr(self.canine, attr)

def click_creature(creature):
    """
    React to a click by showing the creature's
    name and what is says
    """

    return (creature.name, creature.make_noise())