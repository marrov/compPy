class Fruit:
    """A fruit object class"""

    def __init__(self, name):
        print("entering Fruit.__init__")
        self.name = name

    def __str__(self):
        print("entering Fruit.__str__")
        #return "%s tastes sweet!" % self.name
        return f"{self.name} tastes sweet!"

class Citrus(Fruit):
    def __str__(self):
        print("entering Citrus.__str__")
        return "%s tastes sour" % self.name


class FruitWithTaste(Fruit):
    """ A fruit object class with taste"""

    def __init__(self, name, taste="sweet"):
        print("entering FruitWithTaste.__init__")
        Fruit.__init__(self, name)
        self.taste = taste

    def __str__(self):
        print("entering FruitWithTaste.__str__")
        return "%s tastes %s!" % (self.name, self.taste)
