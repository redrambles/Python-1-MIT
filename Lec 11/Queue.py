class Queue(object):

    def __init__(self):
        self.vals = []

    def insert(self, e):
        '''inserts an element 'e' at the back of the list'''
        return self.vals.append(e)

    def remove(self):
        '''removes the element that element at the front of the list
        and Raises a ValueError if the list is empty'''
        try:
            return self.vals.pop(0)
        except:
            raise ValueError()

    
