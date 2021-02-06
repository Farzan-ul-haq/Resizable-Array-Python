
class ResizableArray:
    def __init__(self, size):
        self.size = size
        self.no_of_elements = 0
        self.array = [None for i in range(self.size)]
        # self.

    
    def insert(self, index, value):
        '''
        Insert the value at the given index of an array
        '''
        if index > self.no_of_elements:

    def update(self, index, value):
        '''
        Update the value at the given index of an array
        '''

    def get(self, index):
        '''
        Returns the value from the given index
        '''
    
    def remove(self, index):
        '''
        Remove the value from the given index
        '''

    def printarray(self):
        '''
        print the whole array
        '''
        return self.array

    def traverse(self):
        '''
        Print all the values of an array
        '''

    def resize(self):
        '''
        Resize/shrink the array
        '''
