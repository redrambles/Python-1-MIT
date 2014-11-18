class intSet(object):
    '''An intSet is a set of integers
    The value is represented by a list of ints: self.vals
    Each int in the set occurs in self.vals exactly once.'''

    def __init__(self):
        '''Create an empty list of integers'''
        self.vals = []

    def insert(self, e):
        '''Assumes e is an integer and inserts e into self'''
        if not e in self.vals:
            self.vals.append(e)

    def member(self,e):
        '''Assumes e is an integer and
        Returns True if e is in self.vals and False otherwise'''
        return e in self.vals

    def remove(self,e):
        '''Removes e from self.vals and Raises ValueError if e
        is not in self.vals'''
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found.')

    def intersect(self, other):
        '''Returns a new intSet of integers that appear in both
        self and other'''

        assert type(other) == type(self)
        common = intSet()
        
        for val in self.vals:
            if other.member(val):
                common.insert(val)

        return common

    def __len__(self):
        '''returns the length of the set.'''
        return len(self.vals)

    def __str__(self):
        '''Returns a string representation of self'''
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
