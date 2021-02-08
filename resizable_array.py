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
        elif value == None:
            return 'You can not set value to None'
        else:
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
        if self.array[index] == None:
            return "Array Index is Already None"

        elif index == self.no_of_elements:
            self.array[index] = None
            self.no_of_elements -= 1
        elif index == 0:
            self.newarray = [None for i in range(self.size)]
            for i in range(len(self.newarray)-1):
                self.newarray[i] = self.array[i+1]
            self.array = self.newarray
            self.no_of_elements -=1
        else:
            self.newarray = [None for i in range(self.size)]
            self.removed_array  = self.array[:index] + self.array[index:]
            for i in range(len(self.removed_array)):
                self.newarray[i] = self.removed_array[i]
            self.array = self.newarray
            self.no_of_elements -=1

        if self.no_of_elements*2 == self.size:
            self.resize('shrink')
            




        
        


    def traverse(self):
        '''
        Print all the values of an array
        '''
        return self.array
        print('\n*********************')

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
            print('Array Has Been Resized(Expanded)')
        if operation == 'shrink':
            self.size //= 2
            self.newarray = [None for i in range(self.size)]
            for i in range(len(self.newarray)):
                self.newarray[i] = self.array[i]
            self.array = self.newarray
            print('Array Has Been Resized(Shrink)')
        
            
obj = ResizableArray(4)
print('\nINSERT========')
obj.insert(0,10)
obj.insert(1,9)
obj.insert(2,8)
obj.insert(3,7)
print('***********ARRAY**********')
print(obj.traverse())
print('\n*********************')
print('\nINSERT FOR EXPAND========')
obj.insert(4,40)
print('***********ARRAY**********')
print(obj.traverse())
print('\n*********************')

print('\nUPDATE========')
obj.update(0,20)
print('***********ARRAY**********')
print(obj.traverse())
print('\n*********************')

print('\nREMOVE========')
obj.remove(0)
print('***********ARRAY**********')
print(obj.traverse())
print('\n*********************')
print('\nREMOVE FOR SHRINK========')
obj.remove(2)
print('***********ARRAY**********')
print(obj.traverse())
print('\n*********************')
obj.remove(2)
print('***********ARRAY**********')
print(obj.traverse())
print('\n*********************')
