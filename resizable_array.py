
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
        if self.size == self.no_of_elements:
            self.resize('expand')
        if index > self.no_of_elements:
            return 'Your array Has not Reached to this index yet'
        if self.size != self.no_of_elements:
            # insert at first :O(n)
            if index == 0:
                break_array = self.array[:self.no_of_elements+1]
                self.array[0] = value
                for i in range(len(break_array)):
                    self.array[i+1] = break_array[i]
                self.no_of_elements += 1
            # insert at end :O(1)
            elif index == self.no_of_elements:
                self.array[index] = value
                self.no_of_elements += 1
            # insert at middle :O(n)
            else:
                break_array = self.array[index:self.no_of_elements]
                self.array[index] = value
                self.no_of_elements += 1
                for i in range(len(break_array)):
                    self.array[index + i + 1] = break_array[i]
                
        

    def update(self, index, value):
        '''
        Update the value at the given index of an array
        '''
        if index > self.no_of_elements:
            return 'Array Has not Reached To It Index'
        self.array[index]=value

    def get(self, index):
        '''
        Returns the value from the given index
        '''
        if index > self.no_of_elements:
            return 'Array Has not Reached To It Index'
        return self.array[index] 

    def remove(self, index):
        '''
        Remove the value from the given index
        '''
        


    def traverse(self):
        '''
        Print all the values of an array
        '''
        for i in self.array:
            print(f'{i}',end=' ')

    def resize(self,operation):
        '''
        Expand/shrink the array
        '''
        if operation == 'expand':
            self.size *= 2
            self.newarray = [None for i in range(self.size)]
            for i in range(len(self.array)):
                self.newarray[i] = self.array[i]
            self.array = self.newarray
            print('Array Has Been Resized')
        
            
obj = ResizableArray(4)
obj.insert(0,10)
obj.insert(1,9)
obj.insert(2,8)
obj.insert(3,7)
obj.insert(4,40)
obj.update(0,20)
