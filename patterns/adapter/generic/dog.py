class Dog(object):
    """
    A representation of a dog in 2D Land
    has a different function name for what in our code is make_noise()
    """
    def __init__(self, name):
        self.name = name
    def bark(self):
        return "woof"