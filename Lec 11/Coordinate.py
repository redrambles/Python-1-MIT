import math

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __eq__(self, other):
        # Returns True if coordinates refer to same point in the plane
        # check that they have the same type
        assert type(other) == type(self)
        # Since `other` is the same type, test if coordinates are equal
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'








## Want to determine the distance between this and another point ##

    #def distance(self, other):## this won't work without a sq function
        #return math.sqrt(sq(self.x - other.x) + sq(self.y - other.y))
    


###

##c = Coordinate(3, 4)
##
##origin = Coordinate(0, 0)
##
##print isinstance(c, Coordinate)
##
##print isinstance(origin, Coordinate)
##
##print type(c)
##
##print type(origin)
##
##print type(Coordinate)
