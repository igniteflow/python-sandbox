""" 
Uses a generic Adapter object where the creature and function name are passed 
as instantiation params
"""

class Person(object):
    """A representation of a person in 2D Land"""
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        return "hello"

class CreatureAdapter(object):
    """Adapts a creature for clients in 2D Land"""
    def __init__(self, creature, make_noise):
        """Pass in the function to use as 'make_noise'"""
        self.creature = creature
        self.make_noise = make_noise
    def __getattr__(self, attr):
        """Everything else is delegated to the object"""
        return getattr(self.creature, attr)

def click_creature(creature):
    """
    React to a click by showing the creature's
    name and what is says
    """

    return (creature.name, creature.make_noise())